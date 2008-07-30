Name:          vorbisspi
Summary:       Ogg Vorbis sound engine
Version:       1.0.2
Release:       %mkrel 3
License:       LGPL
Group:	       Sound
Source0:       %name%version.tar.bz2
URL: 	       http://www.javazoom.net/vorbisspi/sources.html
BuildArch:     noarch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: ant
BuildRequires: java-devel-gcj

%description
VorbisSPI  is a SPI (Service Provider Interface - or "Driver" for 
JavaSound API) that adds Ogg Vorbis audio format format to the Java 
Platform (J2SE). It is based on JOrbis, an open source Vorbis library.

%files 
%defattr(-,root,root)
%{_javadir}/vorbisspi1.0.2.jar
%{_javadir}/vorbisspi.jar

#--------------------------------------------------------------------

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java

%description javadoc
Javadoc for %{name}.

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/*

#--------------------------------------------------------------------

%prep
rm -fr %buildroot
%setup -q -n VorbisSPI1.0.2

%build
%{ant} all

%install
install -dm 755 %buildroot%{_javadir}
cp -f vorbisspi1.0.2.jar %buildroot%{_javadir}/

# jars
install -m644 %{name}%{version}.jar -D %{buildroot}%{_javadir}/%{name}%{version}.jar
ln -s %{name}%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -r docs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%clean
rm -fr %buildroot
