import React from "react";
import { Card, CardBody, Row } from "reactstrap";
import FadeIn from "react-fade-in";

export default ({ content, typing }) => {
    return (
        <Row tag={FadeIn} className="d-flex justify-content-start my-1">
            <Card>
                <CardBody className="py-2 px-3">{typing ? "Typing..." : content}</CardBody>
            </Card>
        </Row>
    );
};
