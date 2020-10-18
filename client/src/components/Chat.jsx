import React from "react";
import { Container, Input, Button } from "reactstrap";

import InMessage from "./InMessage";
import OutMessage from "./OutMessage";

export default () => {
    var messages = [
        {
            type: "in",
            content: "im1",
        },
        {
            type: "out",
            content: "om1",
        },
        {
            type: "in",
            content: "im2",
        },
    ];

    return (
        <Container fluid className="d-flex flex-column chatbar justify-content-between py-3">
            <Container fluid>
                {messages.map((message) =>
                    message.type === "in" ? <InMessage {...message} /> : <OutMessage {...message} />
                )}
            </Container>
            <Container fluid className="d-flex flex-row px-0">
                <Input type="text" />
                <Button color="primary" className="ml-2">
                    Send
                </Button>
            </Container>
        </Container>
    );
};
