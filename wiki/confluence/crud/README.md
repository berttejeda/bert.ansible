# Overview

This is a role for creating/updating/deleting Atlassian Confluence wiki pages.

# Requirements

The role makes use of the `markdown2` python package, and so requires the module be installed.

You can execute `pip install markdown2` on the ansible controller to satisfy this requirement.

# Usage Examples

## Via ansible-playbook command

* Create/Update a confluence page from an existing file, in your personal confluence space<br />
	`ANSIBLE_ROLES_PATH=. ansible-playbook --connection=local -i localhost, -e confluence_document="README.md" -e confluence_url="http://wiki.example.com" -e page_title="Test-Page0001" -e confluence_space_key="~myusername" -e confluence_username="myusername" -e confluence_password="mypassword" Taskfile.yaml`
* Create/Update a confluence page from an existing file, in the TESTING Confluence Space<br />
	`ANSIBLE_ROLES_PATH=. ansible-playbook --connection=local -i localhost, -e confluence_document="README.md" -e confluence_url="http://wiki.example.com" -e page_title="Test-Page0001" -e confluence_space_key="TESTING" -e confluence_username="myusername" -e confluence_password="mypassword" Taskfile.yaml`
* Create/Update a confluence page from an existing **jinja template**, in the TESTING Confluence Space<br />
	`ANSIBLE_ROLES_PATH=. ansible-playbook --connection=local -i localhost, -e confluence_document="README.md" -e confluence_url="http://wiki.example.com" -e page_title="Test-Page0001" -e confluence_space_key="TESTING" -e confluence_username="myusername" -e confluence_password="mypassword" Taskfile.yaml -e use_jinja_templating="True"`
* Delete a confluence page<br />
	`ANSIBLE_ROLES_PATH=. ansible-playbook --connection=local -i localhost, -e confluence_document="README.md" -e confluence_url="http://wiki.example.com" -e page_title="Test-Page0001" -e confluence_space_key="TESTING" -e confluence_username="myusername" -e confluence_password="mypassword" -e delete_page="True" Taskfile.yaml`

## Via inclusion from another playbook

tasks:
	- name: Create/Update confluence page from an existing file in the TESTING Confluence Space<br />
	  include_role: confluence/crud
	  vars:	
		confluence_document: "README.md" 
		confluence_url: http://wiki.example.com
		page_title: Test-Page0001
		confluence_space_key: TESTING 
		confluence_username: myusername
		confluence_password: mypassword

	- name: Create/Update confluence page from an existing **jinja template**, in the TESTING Confluence Space<br />
	  include_role: confluence/crud
	  vars:	
		confluence_document: "README.md" 
		confluence_url: http://wiki.example.com
		page_title: Test-Page0001
		confluence_space_key: TESTING 
		confluence_username: myusername
		confluence_password: mypassword
		use_jinja_templating="True"

	- name: Delete a confluence page
	  include_role: confluence/crud
	  vars:	
		confluence_url: http://wiki.example.com
		page_title: Test-Page0001
		confluence_space_key: TESTING 
		confluence_username: myusername
		confluence_password: mypassword
		delete_page="True"

## Via tasks (ansible-playbook wrapper)

* Create/Update a confluence page from an existing file, in your personal confluence space<br />
	`tasks run -r http://wiki.example.com -d README.md -s '~myusername' -u [username] -p [password] -t "Some Title"`
* Create/Update a confluence page from an existing file, in the TESTING Confluence Space<br />
	`tasks run -r http://wiki.example.com -d README.md -s 'TESTING' -u [username] -p [password] -t "Some Title"`
* Create/Update a confluence page from an existing **jinja template**, in the TESTING Confluence Space<br />
	`tasks run -r http://wiki.example.com -d README.md -s 'TESTING' -u [username] -p [password] -t "Some Title" --jinja`
* Delete a confluence page
	`tasks run -r http://wiki.example.com -d README.md -s '~myusername' -u [username] -p [password] -t "Some Title" --delete`

# Appendix

## Resources

- [Confluence Wiki Markup - Atlassian Documentation](https://confluence.atlassian.com/doc/confluence-wiki-markup-251003035.html)
- [ansible-taskrunner](https://github.com/berttejeda/ansible-taskrunner)
