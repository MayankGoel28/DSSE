import React from "react";
import { Navbar, NavbarBrand } from "reactstrap";

export default () => {
    return (
        <Navbar light className="custom-bg-primary mb-3">
            <NavbarBrand href="/" className="font-weight-bold custom-fg-primary">
                {/* E-Commerce Search Engine */}
            </NavbarBrand>
        </Navbar>
    );
};
