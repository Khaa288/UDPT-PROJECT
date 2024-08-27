<?php
class ApiRequest {
    public static function get($url, $params){
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response = curl_exec($ch);

        if ($e = curl_error($ch)) {
            echo $e;
        }
            
        else {
            $decode = json_decode($response);
            return $decode;
        }

        curl_close($ch);
    }

    public static function post($url, $params, $body) {
        $ch = curl_init();

        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($body));
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json; charset=UTF-8'));

        $httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $response = curl_exec($ch);

        if ($e = curl_error($ch)) {
            // echo $e;
            return null;
        }
            
        else {
            $decode = json_decode($response);
            return $decode;
        }

        curl_close($ch);
    }
}
?>