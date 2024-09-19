--
-- PostgreSQL database dump
--

-- Dumped from database version 13.16 (Debian 13.16-1.pgdg120+1)
-- Dumped by pg_dump version 15.8 (Debian 15.8-0+deb12u1)

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

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: joro
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO joro;

--
-- Name: prediction_status; Type: TYPE; Schema: public; Owner: joro
--

CREATE TYPE public.prediction_status AS ENUM (
    'pending',
    'correct',
    'incorrect'
);


ALTER TYPE public.prediction_status OWNER TO joro;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO joro;

--
-- Name: interview; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public.interview (
    id integer NOT NULL,
    date date NOT NULL,
    interviewer character varying(100) NOT NULL,
    title character varying(200) NOT NULL,
    link character varying(500) NOT NULL,
    platform character varying(50) NOT NULL,
    description text,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    transcript text
);


ALTER TABLE public.interview OWNER TO joro;

--
-- Name: interview_id_seq; Type: SEQUENCE; Schema: public; Owner: joro
--

CREATE SEQUENCE public.interview_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.interview_id_seq OWNER TO joro;

--
-- Name: interview_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: joro
--

ALTER SEQUENCE public.interview_id_seq OWNED BY public.interview.id;


--
-- Name: interview_prediction; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public.interview_prediction (
    id integer NOT NULL,
    interview_id integer NOT NULL,
    prediction_id integer NOT NULL,
    prediction_date date NOT NULL
);


ALTER TABLE public.interview_prediction OWNER TO joro;

--
-- Name: interview_prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: joro
--

CREATE SEQUENCE public.interview_prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.interview_prediction_id_seq OWNER TO joro;

--
-- Name: interview_prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: joro
--

ALTER SEQUENCE public.interview_prediction_id_seq OWNED BY public.interview_prediction.id;


--
-- Name: prediction; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public.prediction (
    id integer NOT NULL,
    content text NOT NULL,
    resolution_date date,
    status public.prediction_status,
    created_at timestamp without time zone,
    updated_at timestamp without time zone
);


ALTER TABLE public.prediction OWNER TO joro;

--
-- Name: prediction_id_seq; Type: SEQUENCE; Schema: public; Owner: joro
--

CREATE SEQUENCE public.prediction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.prediction_id_seq OWNER TO joro;

--
-- Name: prediction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: joro
--

ALTER SEQUENCE public.prediction_id_seq OWNED BY public.prediction.id;


--
-- Name: token; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public.token (
    id integer NOT NULL,
    token character varying(64) NOT NULL,
    user_id integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    expires_at timestamp without time zone NOT NULL
);


ALTER TABLE public.token OWNER TO joro;

--
-- Name: token_id_seq; Type: SEQUENCE; Schema: public; Owner: joro
--

CREATE SEQUENCE public.token_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.token_id_seq OWNER TO joro;

--
-- Name: token_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: joro
--

ALTER SEQUENCE public.token_id_seq OWNED BY public.token.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: joro
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(80) NOT NULL,
    email character varying(120) NOT NULL,
    password character varying(255) NOT NULL,
    is_admin boolean
);


ALTER TABLE public."user" OWNER TO joro;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: joro
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO joro;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: joro
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: interview id; Type: DEFAULT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview ALTER COLUMN id SET DEFAULT nextval('public.interview_id_seq'::regclass);


--
-- Name: interview_prediction id; Type: DEFAULT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview_prediction ALTER COLUMN id SET DEFAULT nextval('public.interview_prediction_id_seq'::regclass);


--
-- Name: prediction id; Type: DEFAULT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.prediction ALTER COLUMN id SET DEFAULT nextval('public.prediction_id_seq'::regclass);


--
-- Name: token id; Type: DEFAULT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.token ALTER COLUMN id SET DEFAULT nextval('public.token_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public.alembic_version (version_num) FROM stdin;
0a90d14c6a8f
\.


--
-- Data for Name: interview; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public.interview (id, date, interviewer, title, link, platform, description, created_at, updated_at, transcript) FROM stdin;
1	2024-09-04	Joe Rogan	Episode 1882	http"//www.youtube.com	Youtube	great interview	2024-09-14 18:39:36	2024-09-14 18:39:36	\N
2	2024-09-17	Joe Rogan	Elon Musk on AI and the Future	https://example.com/elon-musk-interview	Spotify	Elon Musk discusses artificial intelligence and his vision for the future.	2024-09-17 18:30:30.358607	2024-09-17 18:30:30.358608	This is a sample transcript of the interview...
\.


--
-- Data for Name: interview_prediction; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public.interview_prediction (id, interview_id, prediction_id, prediction_date) FROM stdin;
\.


--
-- Data for Name: prediction; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public.prediction (id, content, resolution_date, status, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: token; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public.token (id, token, user_id, created_at, expires_at) FROM stdin;
11	ba7e0bc722fe12ca894b3bb6143384b71d139ec94a7c6004914df3f002e93a1a	16	2024-09-17 18:30:30.361219	2024-10-17 18:30:30.357691
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: joro
--

COPY public."user" (id, username, email, password, is_admin) FROM stdin;
16	elon_fan	elon_fan@example.com	pbkdf2:sha256:260000$ipSrVivJYSp7zTqY$dbbb4bd4d64d31288d1b454f61fe1c58d2c4851e3404d0b686e3e65c09aaaeeb	t
\.


--
-- Name: interview_id_seq; Type: SEQUENCE SET; Schema: public; Owner: joro
--

SELECT pg_catalog.setval('public.interview_id_seq', 2, true);


--
-- Name: interview_prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: joro
--

SELECT pg_catalog.setval('public.interview_prediction_id_seq', 1, false);


--
-- Name: prediction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: joro
--

SELECT pg_catalog.setval('public.prediction_id_seq', 1, false);


--
-- Name: token_id_seq; Type: SEQUENCE SET; Schema: public; Owner: joro
--

SELECT pg_catalog.setval('public.token_id_seq', 11, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: joro
--

SELECT pg_catalog.setval('public.user_id_seq', 16, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: interview interview_pkey; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview
    ADD CONSTRAINT interview_pkey PRIMARY KEY (id);


--
-- Name: interview_prediction interview_prediction_pkey; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview_prediction
    ADD CONSTRAINT interview_prediction_pkey PRIMARY KEY (id);


--
-- Name: prediction prediction_pkey; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT prediction_pkey PRIMARY KEY (id);


--
-- Name: token token_pkey; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.token
    ADD CONSTRAINT token_pkey PRIMARY KEY (id);


--
-- Name: token token_token_key; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.token
    ADD CONSTRAINT token_token_key UNIQUE (token);


--
-- Name: prediction unique_prediction; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.prediction
    ADD CONSTRAINT unique_prediction UNIQUE (content, resolution_date);


--
-- Name: user user_email_key; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: interview_prediction interview_prediction_interview_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview_prediction
    ADD CONSTRAINT interview_prediction_interview_id_fkey FOREIGN KEY (interview_id) REFERENCES public.interview(id);


--
-- Name: interview_prediction interview_prediction_prediction_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.interview_prediction
    ADD CONSTRAINT interview_prediction_prediction_id_fkey FOREIGN KEY (prediction_id) REFERENCES public.prediction(id);


--
-- Name: token token_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: joro
--

ALTER TABLE ONLY public.token
    ADD CONSTRAINT token_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: joro
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

