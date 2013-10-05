# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=5
inherit qt4-r2

DESCRIPTION="Graphical program used to map keyboard and mouse buttons to gamepad buttons"
HOMEPAGE="https://github.com/Ryochan7/antimicro"
SRC_URI="https://github.com/Ryochan7/antimicro/archive/${PV}.tar.gz -> ${P}.tar.gz"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE=""

DEPEND="x11-libs/libX11
		x11-libs/libXtst
		>=dev-qt/qtcore-4.8:4
		>=dev-qt/qtgui-4.8:4
		=media-libs/libsdl-1.2*[joystick]"
RDEPEND="${DEPEND}"

S=${WORKDIR}/${P}/src

src_configure() {
	eqmake4 INSTALL_PREFIX=/usr antimicro.pro
}

src_compile() {
	emake 
	emake updateqm
}
