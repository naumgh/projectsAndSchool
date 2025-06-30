import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectCompanyPageComponent } from './select-company-page.component';

describe('SelectCompanyPageComponent', () => {
  let component: SelectCompanyPageComponent;
  let fixture: ComponentFixture<SelectCompanyPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SelectCompanyPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelectCompanyPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
