--
-- PostgreSQL database dump
--

-- Dumped from database version 10.23 (Ubuntu 10.23-0ubuntu0.18.04.2+esm1)
-- Dumped by pg_dump version 14.10 (Ubuntu 14.10-0ubuntu0.22.04.1)

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

--
-- Name: campaign; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.campaign (
    cid bigint NOT NULL,
    name character varying(33) NOT NULL,
    campaignbudget real,
    mission text,
    startdate date,
    enddate date,
    campaignannotation text
);


ALTER TABLE public.campaign OWNER TO c370_s053;

--
-- Name: donates; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.donates (
    cid bigint NOT NULL,
    did bigint NOT NULL,
    total real NOT NULL
);


ALTER TABLE public.donates OWNER TO c370_s053;

--
-- Name: donator; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.donator (
    did bigint NOT NULL,
    name character varying(33),
    email character varying(33),
    ddate date,
    cid bigint
);


ALTER TABLE public.donator OWNER TO c370_s053;

--
-- Name: event; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.event (
    evid bigint NOT NULL,
    name character varying(33),
    ddate date,
    location character varying(255),
    cid bigint,
    eventannotation text
);


ALTER TABLE public.event OWNER TO c370_s053;

--
-- Name: expense1; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.expense1 (
    eid bigint NOT NULL,
    name character varying(33),
    edate date,
    total real,
    evid bigint
);


ALTER TABLE public.expense1 OWNER TO c370_s053;

--
-- Name: expense2; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.expense2 (
    eid2 bigint NOT NULL,
    name character varying(33),
    edate date,
    total real,
    phaseid bigint
);


ALTER TABLE public.expense2 OWNER TO c370_s053;

--
-- Name: participates; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.participates (
    cid bigint NOT NULL,
    vid bigint NOT NULL,
    startdate date,
    enddate date,
    role character varying(25),
    participantannotation text
);


ALTER TABLE public.participates OWNER TO c370_s053;

--
-- Name: phase; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.phase (
    phaseid bigint NOT NULL,
    pushmethod character varying(33),
    startdate date,
    enddate date,
    cid bigint,
    phaseannotation text
);


ALTER TABLE public.phase OWNER TO c370_s053;

--
-- Name: volunteer; Type: TABLE; Schema: public; Owner: c370_s053
--

CREATE TABLE public.volunteer (
    vid bigint NOT NULL,
    name character varying(33) NOT NULL,
    email character varying(55) NOT NULL,
    tierlevel integer,
    salary real
);


ALTER TABLE public.volunteer OWNER TO c370_s053;

--
-- Data for Name: campaign; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.campaign (cid, name, campaignbudget, mission, startdate, enddate, campaignannotation) FROM stdin;
103	final-countdown	500	this is the final countdown	2024-01-02	2024-02-02	\N
104	i-just-want-to-slide	2055	parties in the sky like its 2055	2055-01-02	2055-02-02	\N
105	orange-boogaloo	1345	to give oranges to everyone	2022-04-12	2025-04-13	\N
102	idk	2000	idk im having trouble coming up with mission statements	2024-01-02	2024-02-02	BROTHER KARAMASOV
100	green-love	5000	to make trees great again	2024-03-18	2024-04-18	late night, what's the price?
101	generic-protest	4000	we are just protesting to protest	2024-02-11	2024-03-02	now you cant count these bands with me
106	kbar	2341	to provide eco friendly bars	2022-04-13	2022-07-13	\N
\.


--
-- Data for Name: donates; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.donates (cid, did, total) FROM stdin;
100	5000	100
100	5001	10000
100	5002	2000
100	5003	30
100	5004	40
100	5005	50
104	5001	104
105	5003	1355
104	5005	1023
104	5000	10000
106	5004	1234
\.


--
-- Data for Name: donator; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.donator (did, name, email, ddate, cid) FROM stdin;
5000	Naum Hoffman	naumhoffman@gmail.com	2023-03-02	100
5001	Tim Cook	timcook@gmail.com	2023-03-02	100
5002	Bill Gates	billgates@gmail.com	2023-03-02	100
5003	Musa Ali	musaali@gmail.com	2023-03-02	100
5004	Ali Murat	alimurat@gmail.com	2023-03-02	100
5005	Sarp Aki	sarpaki@gmail.com	2023-03-02	100
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.event (evid, name, ddate, location, cid, eventannotation) FROM stdin;
800002	event3	2024-03-25	230 Menzies St #105, Victoria, BC V8V 2G7, Canada	100	\N
800004	event5	2024-02-23	753 Yates St, Victoria, BC V8W 1L6, Canada	101	\N
800000	event1	2024-03-18	1004 Broad St, Victoria, BC V8W 1Z9, Canada	100	she thought she had one
800001	event2	2024-03-23	1227 Broad St, Victoria, BC V8W 2A4, Canada	100	800001
800003	event4	2024-02-18	753 Yates St, Victoria, BC V8W 1L6, Canada	101	prfab
\.


--
-- Data for Name: expense1; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.expense1 (eid, name, edate, total, evid) FROM stdin;
300	transportation	2024-03-02	50	800000
301	beer	2024-03-03	20	800001
302	lunch	2024-03-04	20.3299999	800002
303	seeds	2024-03-07	45.5600014	800003
304	oranges	2024-03-19	55.7599983	800003
305	crispy creme	2024-03-19	55.7599983	800003
\.


--
-- Data for Name: expense2; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.expense2 (eid2, name, edate, total, phaseid) FROM stdin;
600	FORD-F150	2024-03-02	8000.52979	7003
601	dj	2024-03-03	3000.53003	7001
602	signs	2024-03-04	20.3299999	7004
603	postcards	2024-03-07	45.5600014	7004
604	tables	2024-03-19	55.7599983	7000
\.


--
-- Data for Name: participates; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.participates (cid, vid, startdate, enddate, role, participantannotation) FROM stdin;
100	927502	2024-03-18	2024-03-25	Campaign Employee	\N
101	927502	2024-02-11	2024-03-18	Campaign Employee	\N
100	927503	2024-01-02	2024-03-18	Campaign Volunteer	\N
100	927504	2024-01-02	2024-03-18	Campaign Volunteer	\N
100	927505	2024-01-04	2024-03-18	Campaign Volunteer	\N
103	927502	2024-01-02	2024-03-18	Campaign Employee	\N
102	927505	2024-01-02	2024-03-18	Campaign Volunteer	\N
103	927507	2024-01-02	2024-03-18	Campaign Volunteer	\N
104	927508	2055-01-06	2055-01-09	sleepy	\N
102	927506	2024-01-03	2024-03-18	Campaign Volunteer	aint no shame
\.


--
-- Data for Name: phase; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.phase (phaseid, pushmethod, startdate, enddate, cid, phaseannotation) FROM stdin;
7001	second-phase	2023-02-24	2024-03-16	100	\N
7004	third-phase	2024-03-02	2024-03-04	102	\N
7003	fourth-phase	2024-03-06	2024-03-08	100	\N
7000	first-phase	2023-02-15	2023-02-24	100	im wit my gang you diss my gang then you get dropped
7002	final-phase	2024-03-16	2024-03-18	100	gotta roll this weed up
\.


--
-- Data for Name: volunteer; Type: TABLE DATA; Schema: public; Owner: c370_s053
--

COPY public.volunteer (vid, name, email, tierlevel, salary) FROM stdin;
927502	Clark Davidson	clark@gmail.com	2	35
927503	Dave Hoffman	dave@gmail.com	1	\N
927504	Ava Huntington	ava@gmail.com	1	\N
927505	Clack Clarkson	clack@gmail.com	2	\N
927506	Black White	black@gmail.com	1	\N
927507	Ivan Naskov	ots@gmail.com	2	\N
927508	Debil Naskov	Debil@gmail.com	1	\N
927509	musa	musa@gmail.com	1	\N
\.


--
-- Name: campaign campaign_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.campaign
    ADD CONSTRAINT campaign_pkey PRIMARY KEY (cid);


--
-- Name: donates donates_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.donates
    ADD CONSTRAINT donates_pkey PRIMARY KEY (cid, did);


--
-- Name: donator donator_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.donator
    ADD CONSTRAINT donator_pkey PRIMARY KEY (did);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (evid);


--
-- Name: expense1 expense1_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.expense1
    ADD CONSTRAINT expense1_pkey PRIMARY KEY (eid);


--
-- Name: expense2 expense2_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.expense2
    ADD CONSTRAINT expense2_pkey PRIMARY KEY (eid2);


--
-- Name: participates participates_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.participates
    ADD CONSTRAINT participates_pkey PRIMARY KEY (cid, vid);


--
-- Name: phase phase_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.phase
    ADD CONSTRAINT phase_pkey PRIMARY KEY (phaseid);


--
-- Name: volunteer volunteer_pkey; Type: CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.volunteer
    ADD CONSTRAINT volunteer_pkey PRIMARY KEY (vid);


--
-- Name: donates donates_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.donates
    ADD CONSTRAINT donates_cid_fkey FOREIGN KEY (cid) REFERENCES public.campaign(cid);


--
-- Name: donates donates_did_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.donates
    ADD CONSTRAINT donates_did_fkey FOREIGN KEY (did) REFERENCES public.donator(did);


--
-- Name: donator donator_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.donator
    ADD CONSTRAINT donator_cid_fkey FOREIGN KEY (cid) REFERENCES public.campaign(cid);


--
-- Name: event event_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_cid_fkey FOREIGN KEY (cid) REFERENCES public.campaign(cid);


--
-- Name: expense1 expense1_evid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.expense1
    ADD CONSTRAINT expense1_evid_fkey FOREIGN KEY (evid) REFERENCES public.event(evid);


--
-- Name: expense2 expense2_phaseid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.expense2
    ADD CONSTRAINT expense2_phaseid_fkey FOREIGN KEY (phaseid) REFERENCES public.phase(phaseid);


--
-- Name: participates participates_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.participates
    ADD CONSTRAINT participates_cid_fkey FOREIGN KEY (cid) REFERENCES public.campaign(cid);


--
-- Name: participates participates_vid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.participates
    ADD CONSTRAINT participates_vid_fkey FOREIGN KEY (vid) REFERENCES public.volunteer(vid);


--
-- Name: phase phase_cid_fkey; Type: FK CONSTRAINT; Schema: public; Owner: c370_s053
--

ALTER TABLE ONLY public.phase
    ADD CONSTRAINT phase_cid_fkey FOREIGN KEY (cid) REFERENCES public.campaign(cid);


--
-- PostgreSQL database dump complete
--

