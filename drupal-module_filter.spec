%define modname		module_filter
%define drupal_version	7
%define module_version	1.7
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Module Filter module for Drupal
Version:	%{version}
Release:	2
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
BuildArch:	noarch
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}

%description
The modules list page can become quite big when dealing with a fairly large
site or even just a dev site meant for testing new and various modules being
considered. What this module aims to accomplish is the ability to quickly find
the module you are looking for without having to rely on the browsers search
feature which more times than not shows you the module name in the 'Required
by' or 'Depends on' sections of the various modules or even some other location
on the page like a menu item.

When tabs is enabled via the Module Filter's settings page, a new module layout
theme is implemented. This tab layout provides a tab for each package as well
as a tab that will show every module alphabetically. The filter textfield is
available on each tab but currently doesn't support autocomplete.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc CHANGELOG.txt


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.7-1
+ Revision: 813160
- update to 7.x.1.7

* Sat May 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 7.x.1.6-1
+ Revision: 798461
- imported package drupal-module_filter

