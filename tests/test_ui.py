"""Exercise real UI transitions with a host-compiled C harness; no QEMU required."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT/'package/mrbe-launcher/src'
HARNESS = r'''
#include "ui.h"
#include <assert.h>
#include <string.h>
int main(void) {
    MrbeUIState s;
    mrbe_ui_init(&s);
    assert(s.screen == MRBE_SCREEN_HOME && s.focus == MRBE_FOCUS_NAV);
    mrbe_ui_handle_key(&s, MRBE_KEY_DOWN);
    assert(s.focus == MRBE_FOCUS_HERO);
    mrbe_ui_handle_key(&s, MRBE_KEY_DOWN);
    assert(s.focus == MRBE_FOCUS_CONTENT && s.content_row == 0);
    mrbe_ui_handle_key(&s, MRBE_KEY_RIGHT);
    assert(s.content_col == 1);
    mrbe_ui_handle_key(&s, MRBE_KEY_DOWN);
    assert(s.content_row == 1);
    mrbe_ui_handle_key(&s, MRBE_KEY_HOME);
    assert(s.focus == MRBE_FOCUS_NAV && s.nav_index == 1);
    mrbe_ui_handle_key(&s, MRBE_KEY_APPS);
    assert(s.screen == MRBE_SCREEN_APPS);
    mrbe_ui_handle_key(&s, MRBE_KEY_DOWN);
    assert(s.apps_index == 5);
    mrbe_ui_handle_key(&s, MRBE_KEY_ENTER);
    assert(s.show_notice == 1);
    mrbe_ui_handle_key(&s, MRBE_KEY_BACK);
    assert(s.screen == MRBE_SCREEN_HOME);
    mrbe_ui_handle_key(&s, MRBE_KEY_SETTINGS);
    assert(s.screen == MRBE_SCREEN_SETTINGS);
    mrbe_ui_handle_key(&s, MRBE_KEY_DOWN);
    assert(s.settings_index == 1);
    mrbe_ui_handle_key(&s, MRBE_KEY_BACK);
    assert(s.screen == MRBE_SCREEN_HOME);
    assert(strlen(s.notice) < sizeof(s.notice));
    return 0;
}
'''

class TestUI(unittest.TestCase):
    def test_keyboard_navigation(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            (p/'test-ui.c').write_text(HARNESS)
            exe = p/'test-ui'
            proc = subprocess.run(['cc','-std=c11','-Wall','-Wextra','-Werror',
                  '-I',str(SRC),str(p/'test-ui.c'),str(SRC/'ui.c'),
                  str(SRC/'fb.c'),str(SRC/'font.c'),'-o',str(exe)],
                  capture_output=True,text=True)
            self.assertEqual(proc.returncode,0,proc.stderr)
            run = subprocess.run([str(exe)],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)

    def test_launcher_source_version(self):
        self.assertIn('0.4.0',(SRC/'main.c').read_text())
        self.assertIn('MRBE_SCREEN_APPS',(SRC/'ui.h').read_text())
        self.assertIn('mrbe_ui_handle_key',(SRC/'ui.c').read_text())
