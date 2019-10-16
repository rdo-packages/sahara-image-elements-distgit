%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

Name:           sahara-image-elements
Epoch:          1
Version:        11.0.0
Release:        1%{?dist}
Summary:        Image creation tools for Openstack Sahara

License:        ASL 2.0
URL:            https://launchpad.net/sahara
Source0:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz
#

BuildArch:      noarch

BuildRequires: python%{pyver}-devel
BuildRequires: python%{pyver}-setuptools
BuildRequires: python%{pyver}-pbr >= 2.0.0

Requires: dib-utils
Requires: diskimage-builder >= 2.11.0
Requires: rsync
Requires: wget
Requires: qemu-kvm
Requires: qemu-img
Requires: kpartx
Requires: git

%description
Sahara-image-elements provides the ability to create the images necessary to generate data processing clusters
in Sahara.

%prep
%setup -q -n sahara-image-elements-%{upstream_version}

%build
%{pyver_build}

%install
%{pyver_install}

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/sahara-image-create
%{_bindir}/diskimage-create.sh
%{_datadir}/sahara-elements
%{pyver_sitelib}/sahara_image_elements-%{upstream_version}-py?.?.egg-info

%changelog
* Wed Oct 16 2019 RDO <dev@lists.rdoproject.org> 1:11.0.0-1
- Update to 11.0.0

* Mon Sep 30 2019 RDO <dev@lists.rdoproject.org> 1:11.0.0-0.1.0rc1
- Update to 11.0.0.0rc1

