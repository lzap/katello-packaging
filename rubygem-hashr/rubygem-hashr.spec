%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name hashr

Summary: Simple Hash extension to make working with nested hashes
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.22
Release: 5%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/svenfuchs/hashr
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix}rubygems
Requires: %{?scl_prefix}ruby(abi) = 1.9.1
BuildRequires: %{?scl_prefix}rubygems-devel
BuildRequires: %{?scl_prefix}rubygems

%if 0%{?fedora} > 16
BuildRequires: %{?scl_prefix}rubygem(minitest)
# test_declarative is only in F17+
BuildRequires: %{?scl_prefix}rubygem(test_declarative)
%endif

BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Simple Hash extension to make working with nested hashes (e.g. for
configuration) easier and less error-prone.

%package doc
BuildArch:  noarch
Requires:   %{?scl_prefix}%{pkg_name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
%{?scl:scl enable %{scl} "}
gem unpack %{SOURCE0}
%{?scl:"}
%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} "}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:"}

%build
mkdir -p .%{gem_dir}

%{?scl:scl enable %{scl} "}
# Create the gem as gem install only works on a gem file
%{?scl:"}
%{?scl:scl enable %{scl} "}
gem build %{gem_name}.gemspec
%{?scl:"}

%{?scl:scl enable %{scl} "}
gem install -V \
        --local \
        --install-dir ./%{gem_dir} \
        --force \
        --rdoc \
        %{gem_name}-%{version}.gem
%{?scl:"}
rm -rf ./%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
rm %{buildroot}%{gem_instdir}/{README.md,MIT-LICENSE}

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_cache}
%{gem_spec}
%doc MIT-LICENSE

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile*
%{gem_instdir}/Rakefile
%doc README.md
%{gem_instdir}/test

%check
%if 0%{?fedora} > 16
sed -i '/require.*bundler/d' test/test_helper.rb
%{?scl:scl enable %{scl} "}
testrb -Ilib test/*_test.rb
%{?scl:"}
%endif

%changelog
* Thu Sep 12 2013 Jason Montleon <jmontleo@redhat.com> 0.0.22-5
- new package built with tito

* Wed May 08 2013 Brad Buckingham <bbuckingham@redhat.com> 0.0.22-4
- rebuild for sat6 mdp1

* Fri Mar 01 2013 Miroslav Suchý <msuchy@redhat.com> 0.0.22-2
- new package built with tito

* Fri Nov 09 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.22-1
- 874857 - rebase to rubygem-hashr-0.0.22 (msuchy@redhat.com)

* Wed Aug 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-3
- 845799 - -doc subpackage require the main package (msuchy@redhat.com)
- 845799 - move test/ Gemfile* and Rakefile to -doc subpackage
  (msuchy@redhat.com)
- 845799 - simplify test (msuchy@redhat.com)

* Wed Aug 08 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-2
- run test only in F17+ (msuchy@redhat.com)
- 845799 - use test-suite (msuchy@redhat.com)
- 845799 - use rubygems macros (msuchy@redhat.com)
- create subpackage rubygem-hashr-doc (msuchy@redhat.com)
- rubygem-hashr is released under MIT license (msuchy@redhat.com)
- 845799 - use %%global instead %%define (msuchy@redhat.com)

* Sat Aug 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.21-1
- remove generated yardoc (msuchy@redhat.com)
- remove unused macros (msuchy@redhat.com)
- make summary shorter (msuchy@redhat.com)
- rebase to 0.0.21 (msuchy@redhat.com)

* Wed Jul 04 2012 Miroslav Suchý <msuchy@redhat.com> 0.0.19-3
- edit spec for Fedora 17 (msuchy@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> 0.0.19-2
- hashr - backing down to 0.0.19-2 (bbuckingham@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> 0.0.20-1
- hashr spec - update content autogenerated by gen2rpm (bbuckingham@redhat.com)

* Tue Feb 28 2012 Brad Buckingham <bbuckingham@redhat.com> - 0.0.19-1
- Initial package
