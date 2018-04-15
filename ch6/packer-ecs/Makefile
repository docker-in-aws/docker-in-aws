.PHONY: build
.ONESHELL:

ROLE_ARN = $$(aws configure get role_arn)
ROLE_SESSION_NAME = $$(aws configure get role_session_name)

build:
	@ $(if $(AWS_PROFILE),$(call assume_role))
	packer build packer.json

# Dynamically assumes role and injects credentials into environment
get_credential = jq --null-input "$(1)" | jq .Credentials.$(2) -r
define assume_role
	credentials=`aws sts assume-role --role-arn=$(ROLE_ARN) --role-session-name=$(ROLE_SESSION_NAME)`
	export AWS_ACCESS_KEY_ID=`$(call get_credential,$$credentials,AccessKeyId)`
	export AWS_SECRET_ACCESS_KEY=`$(call get_credential,$$credentials,SecretAccessKey)`
	export AWS_SESSION_TOKEN=`$(call get_credential,$$credentials,SessionToken)`
endef