import React from "react";
import { Card, CardBody, Row } from "reactstrap";

export default ({ content }) => {
    return (
        <Row>
            <Card>
                <CardBody>{content}</CardBody>
            </Card>
        </Row>
    );
};
