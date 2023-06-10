
<?php


include "connection.php";
//POST
//UJ SZAVAZAT LETREHOZASA
/*
function record_vote($kerdes_id,$voter_name, $vote, $kerdes){
    $conn = GetCon();

    $sql = "INSERT INTO szavazatok (kerdes_id,szavazoNeve, valasz,kerdes ) VALUES ('$kerdes_id', '$voter_name', '$vote','$kerdes')";

    if ($conn->query($sql) === TRUE) {
        echo "Vote created successfully". PHP_EOL;
        
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error . PHP_EOL;
    }

    // Close_con($conn);
} */

//GET
//SZAVAZAT LEKERESE SZAVAZO NEVE ALAPJAN
function get_vote_by_voter($voter_name){
    $conn = GetCon();

    $sql = "SELECT szavazoNeve, szavazat FROM szavazatok WHERE szavazoNeve = $voter_name";
    $result = $conn->query($sql);

    if ($result) {
        return "Szavazo: " . $result[0] . ", Szavazat: " . $result[1];
    } else {
        return "No vote found for the specified voter.";
    }

    // Close_con($conn);
}



/// Kérdések válaszainak százalékos eloszlásának lekérése
function get_question_answer_percentages() {
    $conn = GetCon();

    $sql = "SELECT kerdes, valasz, (COUNT(*) / (SELECT COUNT(*) FROM szavazatok WHERE kerdes = s.kerdes)) * 100 AS szazalek
            FROM szavazatok s
            GROUP BY kerdes, valasz";

    try {
        $stmt = $conn->prepare($sql);
        $stmt->execute();
        $result = $stmt->get_result();

        $questionAnswerPercentages = array();

        while ($row = $result->fetch_assoc()) {
            $kerdes = $row['kerdes'];
            $valasz = $row['valasz'];
            $szazalek = $row['szazalek'];

            if (!isset($questionAnswerPercentages[$kerdes])) {
                $questionAnswerPercentages[$kerdes] = array();
            }

            $questionAnswerPercentages[$kerdes][$valasz] = $szazalek;
        }

        return $questionAnswerPercentages;
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }

    Close_con($conn);
}

function getQuestion(){
    $conn = GetCon();

    $sql = "SELECT kerdes FROM kerdes";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        // $ret = "kerdes_id: " . $row["kerdes_id"]. " - kerdes: " . $row["kerdes"]. "<br>";
		$ret = $row;
    } else {
        $ret = "Client not found!";
    }

    // CloseCon($conn);
    return $ret;
}


?>