Summary:	Practical Query Analysis
Summary(pl):	Praktyczny analizator zapytañ
Name:		pqa
Version:	1.5
Release:	0.2
License:	BSD
Group:		Development/Languages
Source0:	http://pgfoundry.org/frs/download.php/155/%{name}-%{version}.zip
# Source0-md5:	1e1429994a5b46df6558d241422cfc50
URL:		http://pqa.projects.postgresql.org/
BuildRequires:	sed >= 4.0
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application allowing you to analyze the queries of PostgreSQL or MySQL
database to see if they can be improved.

%description -l pl
Aplikacja ta pozwaja ci analizowaæ zapytania wysy³ane do baz dancyh
PostgreSQLa lub MySQLa aby zaobaczyæ czy mo¿na je ulepszyæ.

%prep
%setup -q
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
