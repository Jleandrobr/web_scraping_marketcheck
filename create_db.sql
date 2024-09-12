CREATE TABLE Supermercados (
    id SERIAL PRIMARY KEY,
    nome_mercado VARCHAR(255) NOT NULL,
    website VARCHAR(255),
    localizacao VARCHAR(255),
	horario_funcionamento VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE Produtos (
    id SERIAL PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
	link_to_item VARCHAR(255),
	image_url VARCHAR(255),
	preco NUMERIC(10, 2) NOT NULL,
    categoria VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ProdutosPreco (
    id SERIAL PRIMARY KEY,
    produto_id INT REFERENCES Produtos(id) ON DELETE CASCADE,
    supermercado_id INT REFERENCES Supermercados(id) ON DELETE CASCADE,
    preco NUMERIC(10, 2) NOT NULL,
    date_scraped TIMESTAMP DEFAULT NOW(),
    promocao BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);


-- Trigger para atualizar o campo updated_at na tabela Mercados
CREATE OR REPLACE FUNCTION update_supermercados_updated_at()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_supermercados_updated_at
BEFORE UPDATE ON Supermercados
FOR EACH ROW
EXECUTE FUNCTION update_supermercados_updated_at();

-- Trigger para atualizar o campo updated_at na tabela Produtos
CREATE OR REPLACE FUNCTION update_produtos_updated_at()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_produtos_updated_at
BEFORE UPDATE ON Produtos
FOR EACH ROW
EXECUTE FUNCTION update_produtos_updated_at();

-- Trigger para atualizar o campo updated_at na tabela ProdutosPreco
CREATE OR REPLACE FUNCTION update_produtospreco_updated_at()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = NOW();
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER set_produtospreco_updated_at
BEFORE UPDATE ON ProdutosPreco
FOR EACH ROW
EXECUTE FUNCTION update_produtospreco_updated_at();