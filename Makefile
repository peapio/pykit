APP=cve-ease
VERSION=0.1.1
RELEASE=1
DESTDIR=
PYTHON_LIB=$(shell python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
LIB_DIR=$(PYTHON_LIB)/cve_ease

.PHONY: default help version
default:
	@echo ""
	@echo "Makefile for $(APP)"
	@echo "Maintainer: yutianqiang <yutianqiang@chinaredflag.cn>"
	@echo ""
	@echo "help            show help info(default)"
	@echo "kill            kill cve-ease program"
	@echo "install         install cve-ease directly"
	@echo "uninstall       uninstall cve-ease directly"

help: default

version:
	@echo "VERSION:$(VERSION)"
	@echo "RELEASE:$(RELEASE)"
	@echo "PYTHON_LIB:$(PYTHON_LIB)"
	@echo "APP_LIB:$(LIB_DIR)"


.PHONY: kill install uninstall

kill:
	@pkill -x cve-ease || :
	@echo "kill done!"

install: kill
	@echo "* install cve-ease..."
	mkdir -p ${DESTDIR}/usr/bin &> /dev/null || :
	mkdir -p ${DESTDIR}/etc/cve-ease &> /dev/null || :
	# mkdir -p ${DESTDIR}/usr/lib/systemd/system &> /dev/null || :
	mkdir -p ${DESTDIR}/var/log/cve-ease &> /dev/null || :
	mkdir -p ${DESTDIR}/$(LIB_DIR) &> /dev/null || :
	mkdir -p ${DESTDIR}/usr/share/cve-ease &> /dev/null || :
	mkdir -p ${DESTDIR}/tmp/cve-ease/whl &> /dev/null || :
	install -v -m 644  cve-ease.cfg ${DESTDIR}/etc/cve-ease
	install -v -m 755  cve-ease.py ${DESTDIR}/usr/bin/cve-ease
	# install -v -m 644  cve-ease.service ${DESTDIR}/usr/lib/systemd/system/
	# install -v -m 644  cve-ease.timer ${DESTDIR}/usr/lib/systemd/system/
	cd site-packages/cve_ease/ && find . -type f -exec install -Dm 644 "{}" "${DESTDIR}/$(LIB_DIR)/{}" \;
	cd whl/ && find . -type f -exec install -Dm 644 "{}" "${DESTDIR}/tmp/cve-ease/whl/{}" \;
	# @systemctl daemon-reload || :
	@echo "* Install cve-ease Success!"

uninstall:
	rm -rf ${DESTDIR}/etc/cve-ease
	rm -f ${DESTDIR}/usr/bin/cve-ease
	# rm -f ${DESTDIR}/usr/lib/systemd/system/cve-ease.service
	# rm -f ${DESTDIR}/usr/lib/systemd/system/cve-ease.timer
	rm -rf ${DESTDIR}/$(LIB_DIR)
	# @systemctl daemon-reload || :
	@echo "* Uninstall cve-ease Success!"

