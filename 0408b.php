<?php
header("Content-Type: text/html; charset=utf-8");
$result = null;
$error = null;

if (isset($_GET['sub'])) {
    $num1 = isset($_GET['num1']) ? $_GET['num1'] : '';
    $num2 = isset($_GET['num2']) ? $_GET['num2'] : '';
    $operator = isset($_GET['ysf']) ? $_GET['ysf'] : '+';

    // 输入验证
    if (!is_numeric($num1) || !is_numeric($num2)) {
        $error = "必须输入有效数字";
    } else {
        $num1 = (float)$num1;
        $num2 = (float)$num2;
        
        switch ($operator) {
            case '+':
                $result = $num1 + $num2;
                break;
            case '-':
                $result = $num1 - $num2;
                break;
            case '*':
                $result = $num1 * $num2;
                break;
            case '/':
                if ($num2 == 0) {
                    $error = "除数不能为零";
                } else {
                    $result = $num1 / $num2;
                }
                break;
            default:
                $error = "无效运算符";
        }
    }
}
?>

<table align="center" border="1" width="500">
    <form method="get">
        <tr>
            <td colspan="4" align=center border="0"><h1>计算器</h1></td>
        </tr>
        <tr>
            <td>
                <input type="text" 
                       name="num1" 
                       value="<?php echo htmlspecialchars(isset($num1) ? $num1 : ''); ?>" 
                       size="5">
            </td>
            <td>
                <select name="ysf">
                    <option value="+" <?php echo (isset($operator) && $operator == '+') ? 'selected' : ''; ?>>加</option>
                    <option value="-" <?php echo (isset($operator) && $operator == '-') ? 'selected' : ''; ?>>减</option>
                    <option value="*" <?php echo (isset($operator) && $operator == '*') ? 'selected' : ''; ?>>乘</option>
                    <option value="/" <?php echo (isset($operator) && $operator == '/') ? 'selected' : ''; ?>>除</option>
                </select>
            </td>
            <td>
                <input type="text" 
                       name="num2" 
                       value="<?php echo htmlspecialchars(isset($num2) ? $num2 : ''); ?>" 
                       size="5">
            </td>
            <td>
                <input type="submit" name="sub" value="计算">
            </td>
        </tr>
        <?php if (isset($error)): ?>
            <tr>
                <td colspan="4" style="color:red"><?php echo $error; ?></td>
            </tr>
        <?php elseif (isset($result)): ?>
            <tr>
                <td colspan="4">
                    结果：<?php echo round($result, 4); ?>
                </td>
            </tr>
        <?php endif; ?>
    </form>
</table>