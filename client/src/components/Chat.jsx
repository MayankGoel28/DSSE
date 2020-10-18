import React, { useState } from "react";
import { Container, Input, Button, Form } from "reactstrap";

import InMessage from "./InMessage";
import OutMessage from "./OutMessage";

export default ({ setContent }) => {
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
        if (input === "") return;

        setMessages([...messages, { id: messages.length + 1, type: "out", content: input }]);
        // send input to server; update message list and setContent from response
        setContent([{ title: input }]);

        setInput("");
    };

    return (
        <Container fluid className="d-flex flex-column chatbar justify-content-between py-3">
            <Container fluid className="overflow-auto mb-4">
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
                    <Input
                        autoFocus
                        type="text"
                        value={input}
                        placeholder="Type a message..."
                        onChange={(e) => setInput(e.target.value)}
                    />
                    <Button color="dark" className="ml-2 d-flex flex-column justify-content-center">
                        <img src="/send-white-18dp.svg" alt="Send" />
                    </Button>
                </Form>
            </Container>
        </Container>
    );
};
