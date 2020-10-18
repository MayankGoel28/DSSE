import React, { useState } from "react";
import { Container, Input, Button, Form } from "reactstrap";

import InMessage from "./InMessage";
import OutMessage from "./OutMessage";

export default () => {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState([
        {
            id: 0,
            type: "in",
            content: "im1",
        },
        {
            id: 1,
            type: "out",
            content: "om1",
        },
        {
            id: 2,
            type: "in",
            content: "im2",
        },
    ]);

    const sendMessage = (e) => {
        e.preventDefault();
        console.log(input);
        setMessages([...messages, { id: messages.length + 1, type: "out", content: input }]);
        setInput("");
    };

    return (
        <Container fluid className="d-flex flex-column chatbar justify-content-between py-3">
            <Container fluid>
                {messages.map((message) =>
                    message.type === "in" ? (
                        <InMessage key={message.id} {...message} />
                    ) : (
                        <OutMessage key={message.id} {...message} />
                    )
                )}
            </Container>
            <Container fluid className="px-0">
                <Form className="d-flex flex-row" onSubmit={sendMessage}>
                    <Input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
                    <Button color="secondary" className="ml-2">
                        Send
                    </Button>
                </Form>
            </Container>
        </Container>
    );
};
