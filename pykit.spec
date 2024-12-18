Name:           pykit
Version:        1.0.0
Release:        1
Summary:        pykit tools
URL:            https://www.chinaredflag.cn/
License:        MulanPSL2
Source0:        pykit.tar.gz
AutoReqProv:    no

BuildRequires:  python3
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  coreutils

Requires:       systemd
Requires:       sqlite3
Requires:       coreutils
Requires:       python3
Requires:       python3-requests
Requires:       python3-yamlloader
Requires:       python3-flask
Requires:       python3-sqlalchemy
Requires:       python3-SQLAlchemy-Utils
Requires:       python3-jinja2
Requires:       python3-aiohttp
Requires:       python3-retrying
Requires:       python3-defusedxml
Requires:       python3-pandas

%description

cve-ease project.



Provides:       %{name} = %{version}-%{release}
Group:          System Environment/Daemons

%{?systemd_requires}

%prep
tar -zxvf %{_sourcedir}/%{name}-%{version}.tar.gz 

%build

%install
cd %{_builddir}/%{name}-%{version}
make install DESTDIR=%{buildroot}

%post
pip install /tmp/cve-ease/whl/*.whl

%files
/etc/cve-ease/cve-ease.cfg
%attr(0755,root,root) /usr/bin/cve-ease
%{python3_sitelib}/cve_ease
/var/log/cve-ease
/usr/share/cve-ease
/tmp/cve-ease/whl

%changelog
* Mon Nov 11 2024 aqiiii <aqiiii@yeah.net> - 1.0.0-1
- first publish
