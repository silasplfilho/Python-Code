CREATE TABLE DEPRESSION_TOPIC(
    id varchar not null,
    data jsonb
);

ALTER TABLE ONLY public.depression_topic ALTER COLUMN id SET DEFAULT nextval('public.depression_id_seq'::regclass);

COPY public.depression_topic (id, data) FROM STDIN;
1 '{"title": "TEST", "score": "TEST",  "id": "TEST", "url": "TEST", "comms_num": "TEST", "created": "TEST", "body": "TEST"}'
\.

SELECT pg_catalog.setval('public.depression_id_seq', 1, true);
