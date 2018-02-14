%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           sahara-image-elements
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Image creation tools for Openstack Sahara

License:        ASL 2.0
URL:            https://launchpad.net/sahara
Source0:        https://tarballs.openstack.org/sahara-image-elements/sahara-image-elements-%{version}%{?milestone}.tar.gz
BuildArch:      noarch

BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python2-pbr >= 2.0.0

Requires: dib-utils
Requires: diskimage-builder >= 1.1.2
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
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc AUTHORS LICENSE ChangeLog
%{_bindir}/sahara-image-create
%{_bindir}/diskimage-create.sh
%{_datadir}/sahara-elements
%{python2_sitelib}/sahara_image_elements-%{upstream_version}-py?.?.egg-info

%changelog
