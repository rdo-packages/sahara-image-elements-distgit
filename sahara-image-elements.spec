%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


Name:           sahara-image-elements
Epoch:          1
Version:        12.0.0
Release:        1%{?dist}
Summary:        Image creation tools for Openstack Sahara

License:        ASL 2.0
URL:            https://launchpad.net/sahara
Source0:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz
#

BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr >= 2.0.0

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
%{py3_build}

%install
%{py3_install}

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/sahara-image-create
%{_bindir}/diskimage-create.sh
%{_datadir}/sahara-elements
%{python3_sitelib}/sahara_image_elements-%{upstream_version}-py?.?.egg-info

%changelog
* Wed May 13 2020 RDO <dev@lists.rdoproject.org> 1:12.0.0-1
- Update to 12.0.0

* Tue May 05 2020 RDO <dev@lists.rdoproject.org> 1:12.0.0-0.1.0rc1
- Update to 12.0.0.0rc1

