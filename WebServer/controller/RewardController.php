<?php 
class RewardController
{
    public function collectVoucher() {
        require("./api/Endpoints.php");

        $gift_id = $_REQUEST["giftId"];
        $brand_id = $_REQUEST["brandId"];
        $employee_id = json_decode($_SESSION["AuthUser"])->EmployeeId;

        $body = array (
            'GiftId' => $gift_id,
            'BrandId' => $brand_id,
            'EmployeeId' => $employee_id
        );

        $response = ApiRequest::post($exchange_gift_api, null, $body);

        header("Location: index.php?action=my-reward-management");
    }

    public function sendPoint() {
        require("./api/Endpoints.php");

        $sender_id = json_decode($_SESSION["AuthUser"])->EmployeeId;
        $receiver_id = $_REQUEST["receiver"];
        $points = $_REQUEST["points"];

        $body = array(
            'SenderId' => $sender_id,
            'ReceiverId' => $receiver_id,
            'Point' => $points
        );

        $response = ApiRequest::post($send_point_api, null, $body);

        header("Location: index.php?action=to-send-point");
    }
}
?>