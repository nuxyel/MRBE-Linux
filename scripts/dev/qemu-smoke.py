#!/usr/bin/env python3
"""Boot a headless ARM64 QEMU guest; exit as soon as SysV boot marker appears."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import select
import signal
import subprocess
import sys
import time

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--qemu', default=os.environ.get('QEMU','qemu-system-aarch64'))
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--timeout', type=int, default=int(os.environ.get('SMOKE_TIMEOUT','150')))
    args=parser.parse_args()
    images=args.root/'work/output/images'
    log_dir=args.root/'logs/testes'; log_dir.mkdir(parents=True,exist_ok=True)
    log_path=log_dir/'qemu-boot-latest.log'
    report_path=log_dir/'qemu-smoke-latest.json'
    kernel=images/'Image'; rootfs=images/'rootfs.ext4'
    for f in (kernel,rootfs):
        if not f.is_file() or f.stat().st_size==0:
            print(f'[BLOQUEADO] Imagem ausente: {f}. Rode: make build',file=sys.stderr)
            return 2
    if args.timeout <= 0:
        print('[ERRO] Timeout invalido',file=sys.stderr); return 2
    cmd=[args.qemu,'-M','virt','-cpu','cortex-a53','-smp','2','-m','1024','-accel','tcg',
         '-kernel',str(kernel),'-append','root=/dev/vda rootwait console=ttyAMA0 rw loglevel=4',
         '-drive',f'file={rootfs},if=none,format=raw,id=hd0,snapshot=on',
         '-device','virtio-blk-device,drive=hd0',
         '-netdev','user,id=net0','-device','virtio-net-device,netdev=net0',
         '-display','none','-serial','stdio','-monitor','none']
    started=time.monotonic()
    proc=None
    marker=b'MRBE_BOOT_OK'
    tail=b''
    found=False
    result='FAIL'
    try:
        proc=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                              start_new_session=True,bufsize=0)
        assert proc.stdout is not None
        with log_path.open('wb') as log:
            while time.monotonic()-started < args.timeout:
                if proc.poll() is not None:
                    # Read pending output after exit.
                    extra=proc.stdout.read() or b''
                    log.write(extra)
                    tail=(tail+extra)[-8192:]
                    if marker in tail: found=True
                    break
                readable,_,_=select.select([proc.stdout],[],[],0.3)
                if not readable: continue
                chunk=os.read(proc.stdout.fileno(),8192)
                if not chunk: continue
                log.write(chunk); log.flush()
                tail=(tail+chunk)[-8192:]
                if marker in tail:
                    found=True
                    break
        result='PASS' if found else 'FAIL'
    except (FileNotFoundError,PermissionError) as e:
        result='ERROR'
        print(f'[ERRO] QEMU indisponivel: {e}',file=sys.stderr)
    finally:
        if proc is not None and proc.poll() is None:
            try:
                os.killpg(proc.pid,signal.SIGTERM)
                proc.wait(timeout=5)
            except (ProcessLookupError,subprocess.TimeoutExpired):
                try: os.killpg(proc.pid,signal.SIGKILL)
                except ProcessLookupError: pass
                proc.wait()
        report={'result':result,'marker':'MRBE_BOOT_OK','qemu_memory_mib':1024,
                'elapsed_sec':round(time.monotonic()-started,2),
                'log':str(log_path),'kernel':str(kernel),'rootfs':str(rootfs)}
        report_path.write_text(json.dumps(report,indent=2)+'\n')
    if found:
        print(f'[APROVADO] MRBE_BOOT_OK encontrado; {report["elapsed_sec"]}s. Log: {log_path}')
        return 0
    print(f'[FALHA] Nao foi comprovado o boot. Relatorio: {report_path}',file=sys.stderr)
    if tail:
        print(tail[-2000:].decode('utf-8',errors='replace'),file=sys.stderr)
    return 1

if __name__=='__main__': sys.exit(main())
