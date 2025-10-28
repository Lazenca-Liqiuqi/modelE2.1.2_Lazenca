# ModelE2.1.2_Lazenca 主 Makefile | Main Makefile
# NASA GISS Earth System Model (Lazenca Fork)
# 主构建文件，包含默认目标和帮助信息 | Main build file with default targets and help info

.SUFFIXES:
.PHONY: update help

#
# modelE directory structure | modelE 目录结构
MODEL_E_ROOT = .
MODEL_DIR = $(MODEL_E_ROOT)/model
CONFIG_DIR = $(MODEL_E_ROOT)/config

ifeq ($(VERBOSE_OUTPUT),NO)
  MAKEFLAGS=-s
endif

CURRENT_RELEASE=$(shell [ -s $(MODEL_DIR)/version ] && cat $(MODEL_DIR)/version)

default:
	@echo "All make commands should be executed from 'decks' "
	@echo "directory. Please 'cd decks' before running any commands"
	@echo "所有 make 命令都应该在 'decks' 目录中执行"
	@echo "请在运行任何命令之前先 'cd decks'"

help:
	@echo "ModelE2.1.2_Lazenca Build System Help | 构建系统帮助信息"
	@echo "============================================="
	@echo "This is the main Makefile. For detailed build commands,"
	@echo "please see the model directory Makefile."
	@echo "这是主 Makefile。详细的构建命令，请查看 model 目录下的 Makefile"
	$(MAKE) -C $(MODEL_DIR) help

sinclude $(CONFIG_DIR)/rules.mk

update:
	@echo "CVS Repository Update | CVS 仓库更新"
	@echo "=================================="
	@if [ "$(RELEASE)" = "" ] ; then \
	  echo "You have to specify new release with RELEASE=..." ; \
	  echo "必须使用 RELEASE=... 指定新版本" ; exit 1 ; \
	fi
	@echo "--- Starting automatic update from CVS repository ---"
	@echo "--- 开始从 CVS 仓库自动更新 ---"
	@echo "Checking if current directory tree is a branch | 检查当前目录树是否为分支"
	@if cvs status | grep "Sticky *Tag:.*none" ; then \
	  echo "Some of your files are on the main trunk. Will not update." ; \
	  echo "部分文件在主干上。无法更新。" ; \
	  echo "You need to be on a branch to do automatic updates." ;\
	  echo "需要在分支上才能进行自动更新。" ;\
	  echo "Exiting" ; exit 1 ; \
	fi
	@echo "Checking if the model knows its current release | 检查模型是否知道当前版本"
	@if [ "$(CURRENT_RELEASE)" = "" ] ; then \
	  echo "No information on current release. Exiting." ; \
	  echo "没有当前版本信息。退出。" ; exit 1 ; \
	fi
	@if cvs status -v README | grep $(CURRENT_RELEASE) ; then \
	  echo "Current release: $(CURRENT_RELEASE)" ; \
	  echo "当前版本: $(CURRENT_RELEASE)" ; \
	else \
	  echo "No tag $(CURRENT_RELEASE) in repository." ;\
	  echo "仓库中没有 $(CURRENT_RELEASE) 标签。";\
	  echo "Will not update. Exiting"; exit 1 ; \
	fi
	@echo "Searching repository for specified tag: $(RELEASE)"
	@echo "在仓库中搜索指定标签: $(RELEASE)"
	@if cvs status -v README | grep $(RELEASE) ; then \
	  echo "Found tag: $(RELEASE)" ; \
	  echo "找到标签: $(RELEASE)" ; \
	else \
	  echo "The tag $(RELEASE) is not present in CVS repository" ;\
	  echo "CVS 仓库中没有 $(RELEASE) 标签" ;\
	  echo "Will not update. Exiting"; exit 1 ; \
	fi
	@echo "Checking current directory tree | 检查当前目录树"
	@if cvs status | grep "Status: *Needs" ; then \
	  echo "The files listed above are not up-to-date" ; \
	  echo "上述文件不是最新版本" ; \
	  echo "Do 'cvs update' first. Exiting." ; \
	  echo "请先执行 'cvs update'。退出。" ; exit 1; \
	fi
	@echo "Commiting your latest changes to CVS | 提交最新更改到 CVS"
	@cvs commit -m "last commit before update to $(RELEASE)" ; \
	if [ ! $$? = 0 ] ; then \
	  echo "Something went wrong with commit. Aborting..." ; \
	  echo "提交出错。中止..." ; exit 1 ; \
	fi
	@echo "Just in case, last check before we start the update."
	@echo "最后检查，然后开始更新。"
	@if cvs status | grep "Status:" | grep -v "Up-to-date" ; then \
	  echo "The files listed above are not Up-to-date" ; \
	  echo "上述文件不是最新版本" ; \
	  echo "Can not do automatic update. Aborting." ; \
	  echo "无法自动更新。中止。" ; exit 1 ; \
	fi
	@echo "----------   updating   ----------"
	@echo "----------   开始更新   ----------"
	@echo "(using: -j $(CURRENT_RELEASE) -j $(RELEASE) )"
	@echo "(使用: -j $(CURRENT_RELEASE) -j $(RELEASE) )"
	@cvs update -j $(CURRENT_RELEASE) -j $(RELEASE) ; \
	if [ ! $$? = 0 ] ; then \
	  echo "Something went wrong with update..." ; \
	  echo "更新出现问题..." ; \
	  echo "You have to check it manually. Sorry about that ..." ; \
	  echo "你必须手动检查。很抱歉..." ; \
	  exit 1 ; \
	else \
	  echo "--- Successfully updated to $(RELEASE) ---" ; \
	  echo "--- 成功更新到 $(RELEASE) ---" ; \
	fi
	@echo "Checking for possible conflicts | 检查可能的冲突"
	@if cvs status | grep "Status:.*conflict" ; then \
	  echo "The files listed above had conflicts on merge." ; \
	  echo "上述文件在合并时有冲突。" ; \
	  echo "Please check them. " ; \
	  echo "请检查它们。" ; \
	fi
	@echo "After you check your model for possible conflicts"
	@echo "当你检查了模型的可能冲突后"
	@echo "It will be a good idea to commit this new version to cvs"
	@echo "建议将这个新版本提交到 cvs"
	@echo "with 'cvs commit' "
	@echo "使用 'cvs commit' "
	@echo "----------   finished   ----------"
	@echo "----------   完成   ----------"