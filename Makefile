
DESTDIR=/
PREFIX=/usr

all:
	@# do nothing yet

doc:
	$(MAKE) -f doc/Makefile html

install:
	env python setup.py install --root $(DESTDIR) --prefix $(PREFIX) --exec-prefix $(PREFIX)

.PHONY : doc
.PHONY : install
