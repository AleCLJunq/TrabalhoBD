CREATE OR REPLACE VIEW public.vw_cardapio_diario_completo
 AS
 SELECT c.dia,
    c.refeicao,
    r.nome AS nome_restaurante,
    p.nome AS nome_prato
   FROM nucleo_cardapio c
     JOIN nucleo_restaurante r ON c.restaurante_id = r.id
     JOIN nucleo_cardapio_pratos cp ON c.id = cp.cardapio_id
     JOIN nucleo_pratos p ON cp.pratos_id = p.id
  ORDER BY c.dia DESC, r.nome, p.nome;

ALTER TABLE public.vw_cardapio_diario_completo
    OWNER TO postgres;