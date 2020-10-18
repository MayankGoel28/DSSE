import React from "react";
import { Container, Row, Col } from "reactstrap";

import Chat from "../components/Chat";

export default () => {
    return (
        <Container fluid>
            <Row className="mx-3">
                <Col>
                    <h1> welcome </h1>
                </Col>
                <Col className="border-left" md={4}>
                    <Chat />
                </Col>
            </Row>
        </Container>
    );
};
