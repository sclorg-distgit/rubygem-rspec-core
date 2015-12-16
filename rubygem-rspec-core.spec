%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package rubygem-%{gem_name}}

%global	gem_name	rspec-core

Summary:	Rspec-2 runner and formatters
Name:		%{?scl_prefix}rubygem-%{gem_name}
Version:2.14.5
Release:1%{?dist}

Group:		Development/Languages
License:	MIT
URL:		http://github.com/rspec/rspec-mocks
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	%{?scl_prefix_ruby}ruby(release)
BuildRequires:	%{?scl_prefix_ruby}rubygems-devel
#BuildRequires:	%{?scl_prefix}rubygem(ZenTest)
#BuildRequires:	%{?scl_prefix_ruby}rubygem(rake)
#BuildRequires:	%{?scl_prefix}rubygem(rspec-expectations)
#BuildRequires:	%{?scl_prefix}rubygem(rspec-mocks)

Requires:	%{?scl_prefix_ruby}ruby(release)
# Make the following installed by default
# lib/rspec/core/rake_task
Requires:	%{?scl_prefix_ruby}rubygem(rake)
Provides:	%{?scl_prefix}rubygem(%{gem_name}) = %{version}-%{release}
BuildArch:	noarch

%description
Behaviour Driven Development for Ruby.

%package	doc
Summary:	Documentation for %{pkg_name}
Group:		Documentation
Requires:	%{?scl_prefix}%{pkg_name} = %{version}-%{release}

%description	doc
This package contains documentation for %{pkg_name}.


%prep
%setup -q -c -T

%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# rpmlint
pushd .%{gem_instdir}
grep -rl '^#![ \t]*/usr/bin' ./lib| \
	xargs sed -i -e '\@^#![ \t]*/usr/bin@d'

popd

%build

%install
mkdir -p %{buildroot}%{_prefix}
cp -a .%{_prefix}/* %{buildroot}%{_prefix}/

# Rename autospec to avoid conflict with rspec 1.3
# (anyway this script doesn't seem to be useful)
mv %{buildroot}%{_bindir}/autospec{,2}

%check
pushd .%{gem_instdir}
%{?scl:scl enable %scl - << \EOF}
# tests now require rubygem-aruba, which would require more deps in SCL => sorry
# RUBYOPT=-Ilib exe/rspec spec
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/License.txt
%{_bindir}/autospec2
%{_bindir}/rspec
%{gem_instdir}/exe/
%{gem_libdir}
%exclude %{gem_instdir}/.*
%exclude %{gem_cache}
%{gem_spec}


%files	doc
%doc %{gem_instdir}/*.md
%doc %{gem_docdir}
%{gem_instdir}/features/
%{gem_instdir}/spec/

%changelog
* Fri Jan 16 2015 Josef Stribny <jstribny@redhat.com> - 2.14.5-1
- Update to 2.14.5

* Fri Mar 21 2014 Vít Ondruch <vondruch@redhat.com> - 2.11.1-4
- Rebuid against new scl-utils to depend on -runtime package.
  Resolves: rhbz#1069109

* Tue Nov 19 2013 Josef Stribny <jstribny@redhat.com> - 2.11.1-3
- Add missing dist tag.
- Resolves: rhbz#967006

* Mon May 20 2013 Josef Stribny <jstribny@redhat.com> - 2.11.1-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Jul 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.11.1-1
- Update to Rspec-Core 2.11.1.
- Specfile cleanup

* Fri Mar 30 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.8.0-2
- Rebuilt for scl.

* Sun Jan 22 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8.0-1
- 2.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.4-1
- 2.6.4

* Wed May 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.3-1
- 2.6.3

* Tue May 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.2-2
- Workaround for invalid date format in gemspec file (bug 706914)

* Mon May 23 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.2-1
- 2.6.2

* Mon May 16 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-1
- 2.6.0

* Tue May 10 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.2.rc6
- 2.6.0 rc6

* Tue May  3 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.6.0-0.1.rc4
- 2.6.0 rc4

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org>
- And enable check on rawhide

* Sat Feb 26 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.5.1-3
- More cleanups

* Tue Feb 22 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.5.1-2
- Some misc fixes

* Thu Feb 17 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.5.1-1
- 2.5.1

* Fri Nov 05 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.0.1-1
- Initial package
