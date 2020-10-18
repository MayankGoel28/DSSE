import React from "react";
import { Card, CardBody, Row } from "reactstrap";

export default ({ content }) => {
    return (
        <Row className="d-flex justify-content-end">
            <Card>
                <CardBody className="py-2 px-3">{content}</CardBody>
            </Card>
        </Row>
    );
};
