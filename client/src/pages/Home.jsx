import React, { useState } from "react";
import { Container, Row, Col } from "reactstrap";

import Chat from "../components/Chat";
import Greeting from "../components/Greeting";
import ProductItem from "../components/ProductItem";

export default () => {
    const [content, setContent] = useState([]);

    return (
        <Container fluid>
            <Row className="mx-3">
                <Col>
                    <Container fluid className="overflow-auto" style={{ maxHeight: "90vh" }}>
                        {content.length > 0 ? (
                            <Row>
                                {content.map((item) => (
                                    <Col md={4} className="d-flex" key={item.url}>
                                        <ProductItem {...item} />
                                    </Col>
                                ))}
                            </Row>
                        ) : (
                            <Greeting />
                        )}
                    </Container>
                </Col>
                <Col className="border-md border-left" md={4}>
                    <Chat setContent={setContent} />
                </Col>
            </Row>
        </Container>
    );
};
