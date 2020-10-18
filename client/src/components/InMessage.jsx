import React from "react";
import { Card, CardBody, Row } from "reactstrap";

export default ({ content }) => {
    return (
        <Row className="d-flex justify-content-start my-1">
            <Card>
                <CardBody className="py-2 px-3">{content}</CardBody>
            </Card>
        </Row>
    );
};
