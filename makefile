.PHONY: new

DIR_PATH = challenges/$(dir)
TEMPLATE_DIR= .template/

new:
ifeq ($(dir),)
	@echo "Enter a name for the new directory e.g. make dir=new_dir_name"
else
	@cp -r $(TEMPLATE_DIR)/ $(DIR_PATH)
	@echo Created new challenge directory from template: $(DIR_PATH)/
	@ls -a $(DIR_PATH)
endif