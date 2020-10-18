import React from "react";
import { Card, CardBody, Row } from "reactstrap";

export default ({ content }) => {
    return (
        <Row className="d-flex justify-content-end">
            <Card className="bg-primary">
                <CardBody className="py-2 px-3 text-light">{content}</CardBody>
            </Card>
        </Row>
    );
};
