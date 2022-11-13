BUILDDIR=/root/rpmbuild/BUILD
BUILDROOT=/root/rpmbuild/BUILDROOT
NAME=testtask
VERSION=1.0
END=1.el8.x86_64

all:
	g++ main.cpp -o $(NAME)

install:
	mv $(BUILDDIR)/$(NAME)-$(VERSION)/$(NAME) $(BUILDROOT)/$(NAME)-$(VERSION)-$(END)/usr/bin/
