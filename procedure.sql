CREATE OR REPLACE PROCEDURE sp_registrar_compra(
    p_cliente_cpf VARCHAR,
    p_restaurante_id INT,
    p_valor_compra DECIMAL
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_saldo_atual DECIMAL;
BEGIN
    SELECT saldo INTO v_saldo_atual FROM nucleo_cliente WHERE cpf = p_cliente_cpf;

    IF v_saldo_atual >= p_valor_compra THEN
        UPDATE nucleo_cliente 
        SET saldo = saldo - p_valor_compra 
        WHERE cpf = p_cliente_cpf;
        INSERT INTO nucleo_compra(cliente_id, restaurante_id, valor, data_compra, horario)
        VALUES (p_cliente_cpf, p_restaurante_id, p_valor_compra, CURRENT_DATE, CURRENT_TIME);

        RAISE NOTICE 'Compra de R$ % realizada com sucesso para o cliente %.', p_valor_compra, p_cliente_cpf;
    ELSE
        RAISE NOTICE 'Saldo insuficiente (R$ %) para realizar a compra de R$ %. Nenhuma ação foi tomada.', v_saldo_atual, p_valor_compra;
    END IF;
END;
$$;