Name:           redis
Version:	3.0.7        
Release:        1%{?dist}
Summary:        redis 3.0.7 for LeYou

License:        None 
URL:            None 
Source0:        redis-3.0.7.tar.gz
Source1:	6379.conf
Source2:	redis_6379

BuildRequires:  gcc,make
Requires:       chkconfig
Provides: 	redis==3.0.7

%description
安装redis 3.0.7 for LeYou 内部使用
create by bolin 2017-11-30

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
#install
%{__install} -Dp -m 0755 src/redis-server %{buildroot}%{_sbindir}/redis-server
%{__install} -Dp -m 0755 src/redis-benchmark %{buildroot}%{_bindir}/redis-benchmark
%{__install} -Dp -m 0755 src/redis-cli %{buildroot}%{_bindir}/redis-cli
#config and init
%{__install} -Dp -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/redis/6379.conf
%{__install} -Dp -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/init.d/redis_6379
#pid
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/run
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/log
%{__install} -p -d -m 0755 %{buildroot}/data/redis/6379

%post
#add
/sbin/chkconfig --add redis_6379
/etc/init.d/redis_6379 restart

%files
%defattr(-, root, root, 0755)
%doc
%{_sbindir}/redis-server
%{_bindir}/redis-benchmark
%{_bindir}/redis-cli
%{_sysconfdir}/init.d/redis_6379
%config(noreplace) %{_sysconfdir}/redis/6379.conf

#
%dir /data/redis/6379
%dir %{_localstatedir}/log
%dir %{_localstatedir}/run



%changelog
