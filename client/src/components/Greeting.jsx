import React from "react";
import { Container } from "reactstrap";

export default () => {
    return (
        <Container
            fluid
            className="d-flex flex-column justify-content-center align-items-center greeting-container"
        >
            <h1 className="display-3"> Welcome! </h1>
            <h3 className="mt-3 text-muted"> Message the bot to get started. </h3>
        </Container>
    );
};
