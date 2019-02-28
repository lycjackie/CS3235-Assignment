# tools
CC := gcc
RM := rm -f
CP := cp

# flags
CFLAGS := -ggdb -fno-stack-protector
LDFLAGS :=
LDLIBS :=

# sources
sources := program1.c program2.c program3.c program4.c 
targets := program1 program2 program3 program4 

# gmake magic
.PHONY: default all clean generate

#targets
default: all
all: $(targets)

install: $(targets)
	-$(RM) /tmp/program?
	execstack -s program1
	execstack -s program2
	execstack -s program4
	$(CP) $(targets) /tmp


setuid:
ifeq ($(shell id -u),0)
	chown root:root /tmp/program?
	chmod 4755 /tmp/program?
	echo 0 > /proc/sys/kernel/randomize_va_space
else
	@echo "'make setuid' must be run as root -- use su or a root login!"
endif


clean:
	$(RM) $(targets) $(sources:.c=.o) 


