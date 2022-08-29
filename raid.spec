Name:           raid_create
Version:        1.0
Release:        1%{?dist}
Summary:        bash script

License:        GPLv3+
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
Create raid in via Vagrantfile in virtualbox machine

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_bindir}

cd ~/rpmbuild/BUILD/raid_create-1.0/
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue May 31 2016 Kazay <Kazay@mail.ru> - 1.0
- First bello package
