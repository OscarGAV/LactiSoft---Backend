from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.database import Base, engine
from routers.auth import router as auth_router
from routers import (
    departamentos_router, provincias_router, distritos_router,
    direcciones_router, usuarios_router, telefonos_router,
    conductores_router, inspectores_router, transportes_router,
    roles_empresa_router, tipos_canal_router, empresas_router,
    canales_router, consumidores_router, flotas_router,
    puntos_venta_router, centros_acopio_router, reportes_calidad_router,
    productos_router, detalles_producto_router, ordenes_router,
    cabeceras_factura_router, medios_pago_router, facturas_router,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LactiSoft API",
    description="Backend para la gestion de productos lacteos - LactiSoft",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(departamentos_router)
app.include_router(provincias_router)
app.include_router(distritos_router)
app.include_router(direcciones_router)
app.include_router(usuarios_router)
app.include_router(telefonos_router)
app.include_router(conductores_router)
app.include_router(inspectores_router)
app.include_router(transportes_router)
app.include_router(roles_empresa_router)
app.include_router(tipos_canal_router)
app.include_router(empresas_router)
app.include_router(canales_router)
app.include_router(consumidores_router)
app.include_router(flotas_router)
app.include_router(puntos_venta_router)
app.include_router(centros_acopio_router)
app.include_router(reportes_calidad_router)
app.include_router(productos_router)
app.include_router(detalles_producto_router)
app.include_router(ordenes_router)
app.include_router(cabeceras_factura_router)
app.include_router(medios_pago_router)
app.include_router(facturas_router)


@app.get("/", tags=["Health"])
def health():
    return {"status": "ok", "app": "LactiSoft API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)