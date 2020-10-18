import React, { useState } from "react";
import { Container, Row, Col } from "reactstrap";

import Chat from "../components/Chat";
import Greeting from "../components/Greeting";

export default () => {
    const [content, setContent] = useState([]);

    return (
        <Container fluid>
            <Row className="mx-3">
                <Col>
                    {content.length > 0 ? (
                        <Container fluid>
                            {content.map((item) => (
                                <h1> {item.title} </h1>
                            ))}
                        </Container>
                    ) : (
                        <Greeting />
                    )}
                </Col>
                <Col className="border-md border-left" md={4}>
                    <Chat setContent={setContent} />
                </Col>
            </Row>
        </Container>
    );
};
