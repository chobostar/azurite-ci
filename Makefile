.PHONY: up-azurite
up-azurite:
	docker run -d -p 10000:10000 -p 10001:10001 -p 10002:10002 --rm \
			--name azurite_local \
			--mount type=bind,source=$(CURDIR)/tests/certs,target=/certs \
			mcr.microsoft.com/azure-storage/azurite azurite \
			--blobHost 0.0.0.0  --queueHost 0.0.0.0 --tableHost 0.0.0.0 \
			--cert /certs/public.crt \
			--key /certs/private.key
	sleep 3
	python3 tests/init/create_container.py
