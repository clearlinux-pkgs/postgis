#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : postgis
Version  : 2.5.2
Release  : 8
URL      : https://download.osgeo.org/postgis/source/postgis-2.5.2.tar.gz
Source0  : https://download.osgeo.org/postgis/source/postgis-2.5.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC-BY-2.5 GPL-2.0 MIT
Requires: postgis-bin = %{version}-%{release}
Requires: postgis-data = %{version}-%{release}
Requires: postgis-lib = %{version}-%{release}
Requires: postgis-license = %{version}-%{release}
BuildRequires : CUnit-dev
BuildRequires : ImageMagick
BuildRequires : SFCGAL-dev
BuildRequires : bison
BuildRequires : flex
BuildRequires : gdal-dev
BuildRequires : geos-dev
BuildRequires : grep
BuildRequires : json-c-dev
BuildRequires : jsoncpp-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-bin
BuildRequires : pcre-dev
BuildRequires : pkgconfig(libprotobuf-c)
BuildRequires : postgresql-dev
BuildRequires : proj-dev
BuildRequires : xz-dev

%description
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS 
follows the OpenGIS "Simple Features Specification for SQL" and has been 
certified as compliant with the "Types and Functions" profile.

%package bin
Summary: bin components for the postgis package.
Group: Binaries
Requires: postgis-data = %{version}-%{release}
Requires: postgis-license = %{version}-%{release}

%description bin
bin components for the postgis package.


%package data
Summary: data components for the postgis package.
Group: Data

%description data
data components for the postgis package.


%package dev
Summary: dev components for the postgis package.
Group: Development
Requires: postgis-lib = %{version}-%{release}
Requires: postgis-bin = %{version}-%{release}
Requires: postgis-data = %{version}-%{release}
Provides: postgis-devel = %{version}-%{release}
Requires: postgis = %{version}-%{release}

%description dev
dev components for the postgis package.


%package doc
Summary: doc components for the postgis package.
Group: Documentation

%description doc
doc components for the postgis package.


%package lib
Summary: lib components for the postgis package.
Group: Libraries
Requires: postgis-data = %{version}-%{release}
Requires: postgis-license = %{version}-%{release}

%description lib
lib components for the postgis package.


%package license
Summary: license components for the postgis package.
Group: Default

%description license
license components for the postgis package.


%package staticdev
Summary: staticdev components for the postgis package.
Group: Default
Requires: postgis-dev = %{version}-%{release}

%description staticdev
staticdev components for the postgis package.


%prep
%setup -q -n postgis-2.5.2
cd %{_builddir}/postgis-2.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588615662
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1588615662
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/postgis
cp %{_builddir}/postgis-2.5.2/COPYING %{buildroot}/usr/share/package-licenses/postgis/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/postgis-2.5.2/extensions/address_standardizer/COPYING %{buildroot}/usr/share/package-licenses/postgis/72a08efb60f0505073eef690c6612036bd7e0697
cp %{_builddir}/postgis-2.5.2/extras/tiger_geocoder/COPYING %{buildroot}/usr/share/package-licenses/postgis/dc8f2e570bf431427dbc3bab9d4d551b53a60208
cp %{_builddir}/postgis-2.5.2/postgis/vector_tile.LICENSE %{buildroot}/usr/share/package-licenses/postgis/644a450c6de6d9bd6f346b08a5fc35c887a22847
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pgsql2shp
/usr/bin/raster2pgsql
/usr/bin/shp2pgsql

%files data
%defattr(-,root,root,-)
/usr/share/postgresql/contrib/postgis-2.5/legacy.sql
/usr/share/postgresql/contrib/postgis-2.5/legacy_gist.sql
/usr/share/postgresql/contrib/postgis-2.5/legacy_minimal.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis_comments.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis_for_extension.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis_proc_set_search_path.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis_restore.pl
/usr/share/postgresql/contrib/postgis-2.5/postgis_upgrade.sql
/usr/share/postgresql/contrib/postgis-2.5/postgis_upgrade_for_extension.sql
/usr/share/postgresql/contrib/postgis-2.5/raster_comments.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis_for_extension.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis_legacy.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis_proc_set_search_path.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis_upgrade.sql
/usr/share/postgresql/contrib/postgis-2.5/rtpostgis_upgrade_for_extension.sql
/usr/share/postgresql/contrib/postgis-2.5/sfcgal.sql
/usr/share/postgresql/contrib/postgis-2.5/sfcgal_comments.sql
/usr/share/postgresql/contrib/postgis-2.5/sfcgal_upgrade.sql
/usr/share/postgresql/contrib/postgis-2.5/spatial_ref_sys.sql
/usr/share/postgresql/contrib/postgis-2.5/topology.sql
/usr/share/postgresql/contrib/postgis-2.5/topology_comments.sql
/usr/share/postgresql/contrib/postgis-2.5/topology_upgrade.sql
/usr/share/postgresql/contrib/postgis-2.5/uninstall_legacy.sql
/usr/share/postgresql/contrib/postgis-2.5/uninstall_postgis.sql
/usr/share/postgresql/contrib/postgis-2.5/uninstall_rtpostgis.sql
/usr/share/postgresql/contrib/postgis-2.5/uninstall_sfcgal.sql
/usr/share/postgresql/contrib/postgis-2.5/uninstall_topology.sql
/usr/share/postgresql/extension/address_standardizer--1.0--2.5.2.sql
/usr/share/postgresql/extension/address_standardizer--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/address_standardizer--2.5.2.sql
/usr/share/postgresql/extension/address_standardizer--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/address_standardizer.control
/usr/share/postgresql/extension/address_standardizer.sql
/usr/share/postgresql/extension/address_standardizer_data_us--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/address_standardizer_data_us--2.5.2.sql
/usr/share/postgresql/extension/address_standardizer_data_us--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/address_standardizer_data_us.control
/usr/share/postgresql/extension/address_standardizer_data_us.sql
/usr/share/postgresql/extension/postgis--2.0.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.2--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.3--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.4--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.5--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.6--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.0.7--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.2--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.3--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.4--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.5--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.6--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.7--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.8--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.1.9--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.2--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.3--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.4--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.5--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.6--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.7--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.2.8--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.2--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.3--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.4--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.5--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.6--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.7--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.8--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.3.9--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.2--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.3--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.4--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.5--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.6--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.4.7--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.5.0--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.5.1--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/postgis--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.5.2dev--2.5.2.sql
/usr/share/postgresql/extension/postgis--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/postgis--ANY--2.5.2.sql
/usr/share/postgresql/extension/postgis--unpackaged--2.5.2.sql
/usr/share/postgresql/extension/postgis.control
/usr/share/postgresql/extension/postgis_sfcgal--2.0.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.0.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.1.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.2.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.3.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.4.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.2dev--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--ANY--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal--unpackaged--2.5.2.sql
/usr/share/postgresql/extension/postgis_sfcgal.control
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.0.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.1.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.2.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.3.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.4.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.2dev--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--ANY--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder--unpackaged--2.5.2.sql
/usr/share/postgresql/extension/postgis_tiger_geocoder.control
/usr/share/postgresql/extension/postgis_topology--2.0.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.0.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.1.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.2.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.8--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.3.9--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.2--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.3--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.4--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.5--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.6--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.4.7--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.5.0--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.5.1--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.5.2--2.5.2next.sql
/usr/share/postgresql/extension/postgis_topology--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.5.2dev--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--2.5.2next--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--ANY--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology--unpackaged--2.5.2.sql
/usr/share/postgresql/extension/postgis_topology.control

%files dev
%defattr(-,root,root,-)
/usr/include/liblwgeom.h
/usr/include/liblwgeom_topo.h
/usr/lib64/liblwgeom.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/postgresql/extension/README.address_standardizer

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblwgeom-2.5.so.0
/usr/lib64/liblwgeom-2.5.so.0.0.0
/usr/lib64/postgresql/address_standardizer.so
/usr/lib64/postgresql/postgis-2.5.so
/usr/lib64/postgresql/postgis_topology-2.5.so
/usr/lib64/postgresql/rtpostgis-2.5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/postgis/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/postgis/644a450c6de6d9bd6f346b08a5fc35c887a22847
/usr/share/package-licenses/postgis/72a08efb60f0505073eef690c6612036bd7e0697
/usr/share/package-licenses/postgis/dc8f2e570bf431427dbc3bab9d4d551b53a60208

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblwgeom.a
