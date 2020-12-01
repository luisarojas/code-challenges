.PHONY: new

DIR_PATH = challenges/$(dir)
TEMPLATE_DIR= .template/

.ONESHELL:
new:
ifeq ($(dir),)
	@echo "Enter a name for the new directory e.g. \"make dir=new_challenge_name\""
else
	@cp -r $(TEMPLATE_DIR)/ $(DIR_PATH)
	@echo Created new challenge directory from template: $(DIR_PATH)/
endif

help:
	@echo Run like: \"make dir=new_challenge_name\"