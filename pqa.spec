Summary:	Practical Query Analysis
Summary(pl.UTF-8):	Praktyczny analizator zapytań
Name:		pqa
Version:	1.5
Release:	0.4
License:	BSD
Group:		Development/Languages
Source0:	http://pgfoundry.org/frs/download.php/155/%{name}-%{version}.zip
# Source0-md5:	1e1429994a5b46df6558d241422cfc50
Patch0:		http://pgfoundry.org/tracker/download.php/1000008/132/1000262/45/pqa.rb.patch
URL:		http://pqa.projects.postgresql.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application allowing you to analyze the queries of PostgreSQL or MySQL
database to see if they can be improved.

%description -l pl.UTF-8
Aplikacja ta pozwala analizować zapytania wysyłane do baz danych
PostgreSQL lub MySQL aby zobaczyć czy można je ulepszyć.

%prep
%setup -q
%patch0 -p0

sed -i -e '1s,.*ruby,#!%{_bindir}/ruby,' pqa.rb

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pqa.rb $RPM_BUILD_ROOT%{_bindir}/pqa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README mysql_sample.log pglog_sample.log syslog_sample.log test_pqa.rb
%attr(755,root,root) %{_bindir}/pqa
