--
-- PostgreSQL database dump
--

-- Dumped from database version 16.3
-- Dumped by pg_dump version 16.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: categorias; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categorias (
    id_categoria integer NOT NULL,
    nombre_descrip character varying(80) NOT NULL
);


ALTER TABLE public.categorias OWNER TO postgres;

--
-- Name: Categorias_id_categoria_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Categorias_id_categoria_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Categorias_id_categoria_seq" OWNER TO postgres;

--
-- Name: Categorias_id_categoria_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Categorias_id_categoria_seq" OWNED BY public.categorias.id_categoria;


--
-- Name: compras; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.compras (
    id_compra integer NOT NULL,
    fecha date NOT NULL,
    total integer NOT NULL,
    hora character varying(50) NOT NULL,
    id_usuario integer NOT NULL
);


ALTER TABLE public.compras OWNER TO postgres;

--
-- Name: Compras_id_compra_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Compras_id_compra_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Compras_id_compra_seq" OWNER TO postgres;

--
-- Name: Compras_id_compra_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Compras_id_compra_seq" OWNED BY public.compras.id_compra;


--
-- Name: detalle_compras; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detalle_compras (
    id_detalle integer NOT NULL,
    id_compra integer NOT NULL,
    id_producto bigint NOT NULL,
    cantidad integer NOT NULL,
    precio_unitario numeric(10,2) NOT NULL
);


ALTER TABLE public.detalle_compras OWNER TO postgres;

--
-- Name: Detalle_compra_id_detalle_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Detalle_compra_id_detalle_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Detalle_compra_id_detalle_seq" OWNER TO postgres;

--
-- Name: Detalle_compra_id_detalle_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Detalle_compra_id_detalle_seq" OWNED BY public.detalle_compras.id_detalle;


--
-- Name: detalle_ventas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detalle_ventas (
    id_detalle integer NOT NULL,
    id_venta integer NOT NULL,
    id_producto bigint NOT NULL,
    cantidad integer NOT NULL,
    precio_unitario numeric(10,2) NOT NULL
);


ALTER TABLE public.detalle_ventas OWNER TO postgres;

--
-- Name: Detalle_ventas_id_detalle_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Detalle_ventas_id_detalle_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Detalle_ventas_id_detalle_seq" OWNER TO postgres;

--
-- Name: Detalle_ventas_id_detalle_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Detalle_ventas_id_detalle_seq" OWNED BY public.detalle_ventas.id_detalle;


--
-- Name: productos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.productos (
    id_producto bigint NOT NULL,
    nombre character varying(80) NOT NULL,
    precio_de_compra numeric(10,2) NOT NULL,
    precio_de_venta numeric(10,0) NOT NULL,
    stock integer NOT NULL,
    id_categoria integer NOT NULL,
    id_proveedor integer NOT NULL
);


ALTER TABLE public.productos OWNER TO postgres;

--
-- Name: Productos_id_producto_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Productos_id_producto_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Productos_id_producto_seq" OWNER TO postgres;

--
-- Name: Productos_id_producto_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Productos_id_producto_seq" OWNED BY public.productos.id_producto;


--
-- Name: proveedores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proveedores (
    id_proveedor integer NOT NULL,
    nombre_proveedor character varying(80) NOT NULL,
    telefono bigint NOT NULL,
    mail character varying(80)
);


ALTER TABLE public.proveedores OWNER TO postgres;

--
-- Name: Proveedores_id_proveedor_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Proveedores_id_proveedor_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Proveedores_id_proveedor_seq" OWNER TO postgres;

--
-- Name: Proveedores_id_proveedor_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Proveedores_id_proveedor_seq" OWNED BY public.proveedores.id_proveedor;


--
-- Name: ventas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ventas (
    id_venta integer NOT NULL,
    fecha date NOT NULL,
    total numeric(10,2) NOT NULL,
    hora character varying(50) NOT NULL,
    metodo_pago text NOT NULL,
    id_usuario integer NOT NULL
);


ALTER TABLE public.ventas OWNER TO postgres;

--
-- Name: Ventas_id_venta_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Ventas_id_venta_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Ventas_id_venta_seq" OWNER TO postgres;

--
-- Name: Ventas_id_venta_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Ventas_id_venta_seq" OWNED BY public.ventas.id_venta;


--
-- Name: contrasenas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contrasenas (
    id_contrasena integer NOT NULL,
    id_usuario integer NOT NULL,
    contrasena text NOT NULL
);


ALTER TABLE public.contrasenas OWNER TO postgres;

--
-- Name: contrasenas_id_contrasena_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contrasenas_id_contrasena_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contrasenas_id_contrasena_seq OWNER TO postgres;

--
-- Name: contrasenas_id_contrasena_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contrasenas_id_contrasena_seq OWNED BY public.contrasenas.id_contrasena;


--
-- Name: usuarios; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.usuarios (
    id_usuario integer NOT NULL,
    nombre text NOT NULL,
    admin boolean NOT NULL
);


ALTER TABLE public.usuarios OWNER TO postgres;

--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.usuarios_id_usuario_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.usuarios_id_usuario_seq OWNER TO postgres;

--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.usuarios_id_usuario_seq OWNED BY public.usuarios.id_usuario;


--
-- Name: categorias id_categoria; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias ALTER COLUMN id_categoria SET DEFAULT nextval('public."Categorias_id_categoria_seq"'::regclass);


--
-- Name: compras id_compra; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras ALTER COLUMN id_compra SET DEFAULT nextval('public."Compras_id_compra_seq"'::regclass);


--
-- Name: contrasenas id_contrasena; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contrasenas ALTER COLUMN id_contrasena SET DEFAULT nextval('public.contrasenas_id_contrasena_seq'::regclass);


--
-- Name: detalle_compras id_detalle; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_compras ALTER COLUMN id_detalle SET DEFAULT nextval('public."Detalle_compra_id_detalle_seq"'::regclass);


--
-- Name: detalle_ventas id_detalle; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_ventas ALTER COLUMN id_detalle SET DEFAULT nextval('public."Detalle_ventas_id_detalle_seq"'::regclass);


--
-- Name: productos id_producto; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos ALTER COLUMN id_producto SET DEFAULT nextval('public."Productos_id_producto_seq"'::regclass);


--
-- Name: proveedores id_proveedor; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores ALTER COLUMN id_proveedor SET DEFAULT nextval('public."Proveedores_id_proveedor_seq"'::regclass);


--
-- Name: usuarios id_usuario; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios ALTER COLUMN id_usuario SET DEFAULT nextval('public.usuarios_id_usuario_seq'::regclass);


--
-- Name: ventas id_venta; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ventas ALTER COLUMN id_venta SET DEFAULT nextval('public."Ventas_id_venta_seq"'::regclass);


--
-- Data for Name: categorias; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categorias (id_categoria, nombre_descrip) FROM stdin;
\.


--
-- Data for Name: compras; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.compras (id_compra, fecha, total, hora, id_usuario) FROM stdin;
\.


--
-- Data for Name: contrasenas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.contrasenas (id_contrasena, id_usuario, contrasena) FROM stdin;
\.


--
-- Data for Name: detalle_compras; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detalle_compras (id_detalle, id_compra, id_producto, cantidad, precio_unitario) FROM stdin;
\.


--
-- Data for Name: detalle_ventas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detalle_ventas (id_detalle, id_venta, id_producto, cantidad, precio_unitario) FROM stdin;
\.


--
-- Data for Name: productos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.productos (id_producto, nombre, precio_de_compra, precio_de_venta, stock, id_categoria, id_proveedor) FROM stdin;
\.


--
-- Data for Name: proveedores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.proveedores (id_proveedor, nombre_proveedor, telefono, mail) FROM stdin;
\.


--
-- Data for Name: usuarios; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.usuarios (id_usuario, nombre, admin) FROM stdin;
\.


--
-- Data for Name: ventas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ventas (id_venta, fecha, total, hora, metodo_pago, id_usuario) FROM stdin;
\.


--
-- Name: Categorias_id_categoria_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Categorias_id_categoria_seq"', 68, true);


--
-- Name: Compras_id_compra_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Compras_id_compra_seq"', 89, true);


--
-- Name: Detalle_compra_id_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Detalle_compra_id_detalle_seq"', 93, true);


--
-- Name: Detalle_ventas_id_detalle_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Detalle_ventas_id_detalle_seq"', 191, true);


--
-- Name: Productos_id_producto_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Productos_id_producto_seq"', 120, true);


--
-- Name: Proveedores_id_proveedor_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Proveedores_id_proveedor_seq"', 50, true);


--
-- Name: Ventas_id_venta_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Ventas_id_venta_seq"', 205, true);


--
-- Name: contrasenas_id_contrasena_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.contrasenas_id_contrasena_seq', 4, true);


--
-- Name: usuarios_id_usuario_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.usuarios_id_usuario_seq', 5, true);


--
-- Name: categorias Categorias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT "Categorias_pkey" PRIMARY KEY (id_categoria);


--
-- Name: compras Compras_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT "Compras_pkey" PRIMARY KEY (id_compra);


--
-- Name: detalle_compras Detalle_compra_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_compras
    ADD CONSTRAINT "Detalle_compra_pkey" PRIMARY KEY (id_detalle);


--
-- Name: detalle_ventas Detalle_ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_ventas
    ADD CONSTRAINT "Detalle_ventas_pkey" PRIMARY KEY (id_detalle);


--
-- Name: productos Productos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT "Productos_pkey" PRIMARY KEY (id_producto);


--
-- Name: proveedores Proveedores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT "Proveedores_pkey" PRIMARY KEY (id_proveedor);


--
-- Name: ventas Ventas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT "Ventas_pkey" PRIMARY KEY (id_venta);


--
-- Name: contrasenas contrasenas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contrasenas
    ADD CONSTRAINT contrasenas_pkey PRIMARY KEY (id_contrasena);


--
-- Name: categorias descripcion unica; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT "descripcion unica" UNIQUE (nombre_descrip);


--
-- Name: productos id unico; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT "id unico" UNIQUE (id_producto);


--
-- Name: productos nombre unico; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT "nombre unico" UNIQUE (nombre);


--
-- Name: proveedores nombres unicos; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT "nombres unicos" UNIQUE (nombre_proveedor);


--
-- Name: proveedores telefono unicos; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proveedores
    ADD CONSTRAINT "telefono unicos" UNIQUE (telefono);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (id_usuario);


--
-- Name: productos categoria_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT categoria_id FOREIGN KEY (id_categoria) REFERENCES public.categorias(id_categoria) NOT VALID;


--
-- Name: detalle_compras id_compra; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_compras
    ADD CONSTRAINT id_compra FOREIGN KEY (id_compra) REFERENCES public.compras(id_compra) ON DELETE CASCADE NOT VALID;


--
-- Name: detalle_ventas id_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_ventas
    ADD CONSTRAINT id_product FOREIGN KEY (id_producto) REFERENCES public.productos(id_producto) NOT VALID;


--
-- Name: detalle_compras id_producto; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_compras
    ADD CONSTRAINT id_producto FOREIGN KEY (id_producto) REFERENCES public.productos(id_producto);


--
-- Name: CONSTRAINT id_producto ON detalle_compras; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT id_producto ON public.detalle_compras IS 'trae el id de el producto comprado';


--
-- Name: detalle_ventas id_venta; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle_ventas
    ADD CONSTRAINT id_venta FOREIGN KEY (id_venta) REFERENCES public.ventas(id_venta) ON DELETE CASCADE NOT VALID;


--
-- Name: productos pord_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.productos
    ADD CONSTRAINT pord_id FOREIGN KEY (id_producto) REFERENCES public.productos(id_producto) ON DELETE CASCADE NOT VALID;


--
-- Name: contrasenas usu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contrasenas
    ADD CONSTRAINT usu FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id_usuario) NOT VALID;


--
-- Name: compras usu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.compras
    ADD CONSTRAINT usu FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id_usuario) NOT VALID;


--
-- Name: ventas usu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ventas
    ADD CONSTRAINT usu FOREIGN KEY (id_usuario) REFERENCES public.usuarios(id_usuario) NOT VALID;


--
-- PostgreSQL database dump complete
--

