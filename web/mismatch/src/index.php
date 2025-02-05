<?php
$quotes = [
    "steve" => "The only way to do great work is to love what you do.",
    "nelson" => "It always seems impossible until it’s done.",
    "leonardo" => "Simplicity is the ultimate sophistication.",
    "albert" => "In the middle of every difficulty lies opportunity."
];
$persons = [
    "steve" => "Steve Jobs",
    "nelson" => "Nelson Mandela",
    "leonardo" => "Leonardo da Vinci",
    "albert" => "Albert Einstein"
];

$img = "";
$val = "";
$show = False;
if (array_key_exists("input", $_POST) && array_key_exists("options", $_POST)) {
    $hidden = "n0th1ng_to_s33_h3r3";
    $val = $_POST["input"];
    if ($_POST["input"] === $hidden) {
        echo "<img class='image' src='d4xk30hgv88dchrd.jpg' alt='No image'>";
        exit();
    }
    if (!in_array($_POST["input"], array_values($quotes))) {
        $show = True;
        $val = "";
    }
} 
if (array_key_exists("options", $_POST) && !$show) {
    $val = $quotes[$_POST["options"]];
    switch ($_POST["options"]) {
        case "steve":
            $img = "steve.webp";
            break;
        case "nelson":
            $img = "nelson.webp";
            break;
        case "leonardo":
            $img = "leonardo.webp";
            break;
        case "albert":
            $img = "albert.webp";
            break;
        default:
            echo $_POST["input"] . " is unavailable";
            break;
    } 
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quote Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
            <?php 
            if ($img !== "") {
                echo "<img class='image' src='$img' alt='No image'>";
            }
            ?>
            <form class="form" action="" method="post">
                <label for="options">Choose an option:</label>
                <div class="input-group">
                    <select class="select" name="options" id="options">
                        <option value="" disabled selected>Select an option</option>
                        <?php 
                        foreach ($quotes as $person => $quote) {
                        $fullname = $persons[$person];
                        $selected = array_key_exists('options', $_POST) && $_POST['options'] === $person ? 'selected' : '';
                        echo "<option value='$person' $selected>$fullname</option>";
                        }
                        ?>
                    </select>

                    <?php 
                    if ($val === "") {
                    echo "<input class='input' type='text' name='input' id='inputField' placeholder='Enter text here' value='$val' disabled>";
                    } else {
                    echo "<input class='input' type='text' name='input' id='inputField' placeholder='Enter text here' value='$val'>";
                    }
                    ?>
                </div>
                <?php 
                if ($show) {
                echo "<input hidden value='$hidden' name='hidden'>";
                }
                ?>

                <button class="button" type="submit">Submit</button>
            </form>
    </div>
</body>
</html>
