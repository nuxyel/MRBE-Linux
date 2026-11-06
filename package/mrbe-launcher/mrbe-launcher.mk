################################################################################
# mrbe-launcher - interface TV framebuffer (sem desktop pesado)
################################################################################
MRBE_LAUNCHER_VERSION = 0.4.0
MRBE_LAUNCHER_SITE = $(BR2_EXTERNAL_MRBE_PATH)/package/mrbe-launcher/src
MRBE_LAUNCHER_SITE_METHOD = local
MRBE_LAUNCHER_LICENSE = MIT
MRBE_LAUNCHER_LICENSE_FILES = LICENSE

define MRBE_LAUNCHER_BUILD_CMDS
	$(TARGET_CC) $(TARGET_CFLAGS) -std=c11 -Os -Wall -Wextra -Werror \
		-o $(@D)/mrbe-launcher \
		$(@D)/main.c $(@D)/fb.c $(@D)/font.c \
		$(@D)/input.c $(@D)/ui.c
endef

define MRBE_LAUNCHER_INSTALL_TARGET_CMDS
	$(INSTALL) -D -m 0755 $(@D)/mrbe-launcher \
		$(TARGET_DIR)/usr/bin/mrbe-launcher
	$(INSTALL) -D -m 0644 $(@D)/assets/brasao-256.rgba \
		$(TARGET_DIR)/usr/share/mrbe/brand/brasao-256.rgba
endef

$(eval $(generic-package))
