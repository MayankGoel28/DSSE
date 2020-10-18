import React from "react";
import { Card, CardBody, CardImg, CardFooter, Button } from "reactstrap";

export default (props) => {
    return (
        <Card className="flex-fill my-3">
            <CardImg
                src={props.img === "" ? "/product-placeholder.jpg" : `https://${props.img}`}
                className="product-img p-2"
            />
            <CardBody>
                {props.title}
                {props.price}
                {props.stars} ({props.ratings})
            </CardBody>
            <CardFooter>
                <Button tag="a" href={props.url}>
                    Buy at Walmart
                </Button>
            </CardFooter>
        </Card>
    );
};
